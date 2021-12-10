import struct

from tornado.ioloop import IOLoop

from udpserver import UDPServer
from udpmessage import _DEFAULT_PROCESS_NUM, _UDP_MSG_SIZE_ETHERNET


# >I 4字节  >H 2字节 >B 1字节
class KCPServer(UDPServer):
    def __init__(self, msg_size=_UDP_MSG_SIZE_ETHERNET, process_num=256):
        UDPServer.__init__(self, msg_size, process_num)
        self.conv_id = 1

    async def handle_message(self, sock, data, address):
        if data.startswith(b'kcp'):
            if struct.unpack(">B", data[3:])[0] == 1:
                data = b''.join([data, struct.pack('>I', self.conv_id)])
                await sock.send(data, address)
                self.conv_id += 1
                # todo 做缓存，超时丢弃，没有重新获取convid
        else:
            pass

server = KCPServer()
# server.bind(8888)
server.bind(8887)
server.start()
# server.stop()
IOLoop.current().start()
