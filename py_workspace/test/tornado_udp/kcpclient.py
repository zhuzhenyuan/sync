import socket
import struct

from tornado.ioloop import IOLoop

from kcpmessage import KCPMessage
from udpmessage import _DEFAULT_PROCESS_NUM, UDPMessage, _UDP_MSG_SIZE_ETHERNET


# >I 4字节  >H 2字节 >B 1字节
class KCPClient(KCPMessage):
    def __init__(self,  msg_size=_UDP_MSG_SIZE_ETHERNET, process_size=_DEFAULT_PROCESS_NUM):
        super(KCPClient, self).__init__(UDPMessage(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), process_size), msg_size)

    async def connect(self, address, port):
        super(KCPClient, self).connect(address, port)
        await self.send(b''.join([b'kcp', struct.pack('>B', 1)]))
        ret = await self.recv(8)
        _, self.conv = struct.unpack(">BI", ret[3:])


async def aa():
    # client = await UDPClient().connect('127.0.0.1', 8888)
    client = await KCPClient().connect('127.0.0.1', 8887)


IOLoop.instance().run_sync(aa)
