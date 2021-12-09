from tornado.ioloop import IOLoop

from udpserver import UDPServer


class MyServer(UDPServer):
    # def handle_message(self, sock, data, address):
    #     sock.send(b'Hello, %s!' % data, address)
    async def handle_message(self, sock, data, address):
        a = await sock.send(b'Hello, %s!' % data, address)
        print(a)


server = MyServer()
server.bind(8888)
server.bind(8887)
server.start()
# server.stop()
IOLoop.current().start()
