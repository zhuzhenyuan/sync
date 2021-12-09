from tornado.ioloop import IOLoop

from udpserver import UDPServer


class MyServer(UDPServer):
    def handle_message(self, sock, data, address):
        sock.sendto(b'Hello, %s!' % data, address)


server = MyServer()
server.bind(8888)
server.bind(8887)
server.start()
# server.stop()
IOLoop.current().start()
