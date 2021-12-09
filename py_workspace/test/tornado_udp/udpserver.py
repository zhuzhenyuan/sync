import os
import stat
import errno
import socket
from typing import Any, Optional, List, Callable, Awaitable
from tornado.ioloop import IOLoop
from tornado import process, gen
from tornado.log import app_log

_DEFAULT_BACKLOG = 128
_DEFAULT_RECEIVE = 128

# 接收的数据大小 减去 ip 协议头 以及 UDP 协议头
_RECEIVE_MSG_SIZE_MAX = 65535 - 20 - 8  # 单个数据包最大
_RECEIVE_MSG_SIZE_ETHERNET = 1500 - 20 - 8  # 以太网建议最大
_RECEIVE_MSG_SIZE_INTERNET = 576 - 20 - 8  # 因特网建议最大


def bind_sockets(port: int,
                 address: Optional[str] = None,
                 family: socket.AddressFamily = socket.AF_UNSPEC,
                 backlog: int = _DEFAULT_BACKLOG) -> List[socket.socket]:
    sockets = []
    if address == "":
        address = None
    flags = socket.AI_PASSIVE
    if hasattr(socket, "AI_ADDRCONFIG"):
        flags |= socket.AI_ADDRCONFIG
    for res in set(socket.getaddrinfo(address, port, family, socket.SOCK_DGRAM, 0, flags)):
        af, socktype, proto, canonname, sockaddr = res
        sock = socket.socket(af, socktype, proto)
        # set_close_exec(sock.fileno())  # todo 不知道有啥影响
        if os.name != 'nt':
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if af == socket.AF_INET6:
            if hasattr(socket, "IPPROTO_IPV6"):
                sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
        sock.setblocking(False)
        sock.bind(sockaddr)
        sockets.append(sock)
    return sockets


if hasattr(socket, 'AF_UNIX'):
    def bind_unix_socket(file: str, mode: int = 0o600, backlog: int = 128) -> socket.socket:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        # set_close_exec(sock.fileno())  # todo 不知道有啥影响
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(False)
        try:
            st = os.stat(file)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise
        else:
            if stat.S_ISSOCK(st.st_mode):
                os.remove(file)
            else:
                raise ValueError("File %s exists and is not a socket", file)
        sock.bind(file)
        os.chmod(file, mode)
        sock.listen(backlog)
        return sock


def add_accept_handler(sock: socket.socket,
                       callback: Callable[[socket.socket, bytes, Any], None],
                       receive_num=_DEFAULT_RECEIVE,
                       receive_msg_size=_RECEIVE_MSG_SIZE_MAX) -> None:
    def accept_handler(fd: socket.socket, events: int) -> None:
        # 可以死循环，但是考虑有大量数据包时，其他协程处理会很晚（极限情况可能根本执行不到）,故设置receive最大上限
        for _ in range(receive_num):
            try:
                data, address = sock.recvfrom(receive_msg_size)
            except socket.error as e:
                if e.args[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                    return
                raise
            callback(sock, data, address)

    IOLoop.current().add_handler(sock.fileno(), accept_handler, IOLoop.READ)


class UDPServer(object):
    def __init__(self):
        self._sockets = {}  # type: Dict[int, socket.socket]
        self._pending_sockets = []  # type: List[socket.socket]
        self._started = False
        self._stopped = False
        self._receive_num = _DEFAULT_RECEIVE
        self._receive_msg_size = _RECEIVE_MSG_SIZE_MAX

    def set_default_msg_receive_size(self, size: int):
        self._receive_msg_size = size

    def bind(
            self,
            port: int,
            address: Optional[str] = None,
            family: socket.AddressFamily = socket.AF_UNSPEC,
            backlog: int = 128,
    ) -> None:
        sockets = bind_sockets(port, address=address, family=family, backlog=backlog)
        if self._started:
            self.add_sockets(sockets)
        else:
            self._pending_sockets.extend(sockets)

    def add_sockets(self, sockets):
        for sock in sockets:
            self._sockets[sock.fileno()] = sock  # todo 这里包装一下，就可以异步send了
            add_accept_handler(sock, self._handle_connection, self._receive_num, self._receive_msg_size)

    def add_socket(self, socket: socket.socket) -> None:
        self.add_sockets([socket])

    def start(self, num_processes: Optional[int] = 1, max_restarts: Optional[int] = None) -> None:
        assert not self._started
        self._started = True
        if num_processes != 1:
            process.fork_processes(num_processes, max_restarts)
        sockets = self._pending_sockets
        self._pending_sockets = []
        self.add_sockets(sockets)

    def stop(self) -> None:
        if self._stopped:
            return
        self._stopped = True
        for fd, sock in self._sockets.items():
            assert sock.fileno() == fd
            IOLoop.current().remove_handler(fd)
            sock.close()

    def handle_message(self, sock: socket.socket, data: bytes, address: Any) -> Optional[Awaitable[None]]:
        raise NotImplementedError()
        # sock.sendto(b'Hello, %s!' % data, address)

    def _handle_connection(self, sock: socket.socket, data: bytes, address: Any) -> None:
        try:
            future = self.handle_message(sock, data, address)
            if future is not None:
                IOLoop.current().add_future(
                    gen.convert_yielded(future), lambda f: f.result()
                )
        except Exception:
            app_log.error("Error in connection callback", exc_info=True)

