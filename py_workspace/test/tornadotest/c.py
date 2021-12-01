import asyncio
from datetime import datetime

import tornado
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient


async def aa():
	client = await TCPClient().connect("localhost", 8888)
	# for i in range(2):
	# c = await client.write(b"login\n")
	c = await client.write(b"print\n")
	# d = await client.read_until(b'\n')
	d = await client.read_bytes(50, True)
	print(d)

# IOLoop.instance().run_sync(aa)


