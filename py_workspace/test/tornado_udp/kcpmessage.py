# 0               4   5   6       8 (BYTE)
# +---------------+---+---+-------+
# |     conv      |cmd|frg|  wnd  |
# +---------------+---+---+-------+   8
# |     ts        |     sn        |
# +---------------+---------------+  16
# |     una       |     len       |
# +---------------+---------------+  24
# |                               |
# |        DATA (optional)        |
# |                               |
# +-------------------------------+


# cmd 1 字节: Command.
#     数据报文 IKCP_CMD_PUSH
#     确认报文 IKCP_CMD_ACK
#     窗口探测报文 IKCP_CMD_WASK, 询问对端剩余接收窗口的大小.
#     窗口通知报文 IKCP_CMD_WINS, 通知对端剩余接收窗口的大小.
from typing import Awaitable

from udpmessage import UDPMessage, _DEFAULT_PROCESS_NUM, _UDP_MSG_SIZE_MAX


class KCPPackage(object):
    def __init__(self):
        self.conv = bytes(4)  # conv 4 字节: 连接标识, 前面已经讨论过了.自己实现协商
        self.cmd = bytes(1)  # cmd 1 字节: Command.
        self.frg = bytes(1)  # frg 1 字节: 分片数量. 表示随后还有多少个报文属于同一个包.
        self.wnd = bytes(2)  # wnd 2 字节: 发送方剩余接收窗口的大小.
        self.ts = bytes(4)  # ts 4 字节: 时间戳.
        self.sn = bytes(4)  # sn 4 字节: 报文编号.
        self.una = bytes(4)  # una 4 字节: 发送方的接收缓冲区中最小还未收到的报文段的编号. 也就是说, 编号比它小的报文段都已全部接收.
        self.len = bytes(4)  # len 4 字节: 数据段长度.
        self.data = bytes()  # data: 数据段. 只有数据报文会有这个字段.

        self.node = None  # 链表节点.我们会在3.3节详细讨论.
        self.resendts = 0  # 重传时间戳.超过这个时间表示该报文超时, 需要重传.
        self.rto = 0  # 该报文的RTO.
        self.fastack = 0  # ACK失序次数.也就是KCP Readme中所说的"跳过"次数.
        self.xmit = 0  # 该报文传输的次数.


# >I 4字节  >H 2字节 >B 1字节
class KCPMessage(object):
    def __init__(self, sock: UDPMessage, msg_size):
        self._sock = sock
        self._msg_size = msg_size
        self._remote_address = None

        self.conv = 0

    def __getattr__(self, item):
        return getattr(self._sock, item)

    def connect(self, address, port):
        self._remote_address = (address, port)
        return self

    def pack(self):
        pass

    def unpack(self):
        pass

    # 发送一个完整数据
    def kcp_send(self, data) -> Awaitable[None]:
        # todo 按照self._msg_size分片
        return self._sock.send(data, self._remote_address)

    # 接收一个完整数据
    def kcp_recv(self) -> Awaitable[bytes]:
        # todo 需要处理分片
        return self._sock.recv(self._msg_size)
