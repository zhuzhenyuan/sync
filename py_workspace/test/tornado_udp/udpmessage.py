import errno
import socket
from typing import Awaitable
from collections import deque

from tornado import ioloop
from tornado.ioloop import IOLoop
from tornado.concurrent import Future, future_set_result_unless_cancelled

_DEFAULT_PROCESS_NUM = 128

# 接收的数据大小 减去 ip 协议头 以及 UDP 协议头
_UDP_MSG_SIZE_MAX = 65535 - 20 - 8  # 单个数据包最大
_UDP_MSG_SIZE_ETHERNET = 1500 - 20 - 8  # 以太网建议最大
_UDP_MSG_SIZE_INTERNET = 576 - 20 - 8  # 因特网建议最大


class UDPMessage(object):
    def __init__(self, sock, process_num=_DEFAULT_PROCESS_NUM):
        self.io_loop = IOLoop.current()
        self._process_num = process_num
        self.sock = sock
        self.sock.setblocking(False)
        self._read_buffer = deque()
        self._write_buffer = deque()
        self._state = ioloop.IOLoop.ERROR | ioloop.IOLoop.READ

    def __getattr__(self, item):
        return getattr(self.sock, item)

    def recv(self, size) -> Awaitable[bytes]:
        future = Future()
        # future.add_done_callback(lambda f: f.exception())
        self._read_buffer.append((size, future))
        return future

    def handle_read(self):
        receives = []
        num = min(self._process_num, len(self._read_buffer))
        for _ in range(num):
            size, future = self._read_buffer.popleft()
            try:
                data = self.sock.recv(size)
            except socket.error as e:
                self._read_buffer.appendleft((size, future))
                if e.args[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                    break
                raise
            receives.append((data, future))
        for data, future in receives:
            future_set_result_unless_cancelled(future, data)

    def send(self, data, address) -> Awaitable[None]:
        future = Future()
        # future.add_done_callback(lambda f: f.exception())
        self._write_buffer.append((data, address, future))
        if not self._state & ioloop.IOLoop.WRITE:
            self.io_loop.update_handler(self.sock.fileno(), self._state | ioloop.IOLoop.WRITE)
        return future

    def handle_write(self):
        num = min(self._process_num, len(self._write_buffer))
        socks = []
        for _ in range(num):
            data, address, future = self._write_buffer.popleft()
            self.sock.sendto(data, address)
            socks.append(future)
        for future in socks:
            future_set_result_unless_cancelled(future, None)
        if len(self._write_buffer) <= 0:
            self.io_loop.update_handler(self.sock.fileno(), self._state)
