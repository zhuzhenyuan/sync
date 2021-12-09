from tornado.ioloop import IOLoop

from udpclient import UDPClient


async def aa():
    # client = UDPClient().connect('127.0.0.1', 8888)
    # client = UDPClient().connect('127.0.0.1', 8887)
    client = UDPClient().connect('47.102.125.88', 8888)
    # client = UDPClient().connect('47.102.125.88', 8887)
    for _ in range(10):
        c = await client.send(b"print1\n")
        print(c)
        c = await client.send(b"print2\n")
        print(c)
        d = await client.recv(50)
        print(d)
        c = await client.send(b"print3\n")
        print(c)
        d = await client.recv(50)
        print(d)
        d = await client.recv(50)
        print(d)


IOLoop.instance().run_sync(aa)
