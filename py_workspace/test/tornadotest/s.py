import json

from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError

player_manage = {}


class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        player = None
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
                    "".encode('utf8')
                await stream.write((json.dumps(player)+'\n').encode('utf8'))
            except StreamClosedError:
                break


server = EchoServer()
server.listen(8888)
IOLoop.current().start()
