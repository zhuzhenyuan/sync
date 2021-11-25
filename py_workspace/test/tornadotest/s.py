from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen

player_manage = {}

class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b"\n")
                # print(data)
                if data == b"login\n":
                    player = {
                        'gold': 1000
                    }
                    player_manage[1] = player
                elif data == b"print\n":
                    player = player_manage[1]
                    print(player['gold'])
                await stream.write(data)
            except StreamClosedError:
                break


server = EchoServer()
server.listen(8888)
IOLoop.current().start()