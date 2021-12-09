import collections
import errno
import functools
import socket
import time
from typing import Optional, Awaitable, Union

from tornado import ioloop
from tornado.concurrent import Future, future_set_result_unless_cancelled
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from collections import deque


class UDPMessage(object):
    pass

class UDPClient(object):
    def __init__(self):
        self.io_loop = IOLoop.current()
        self._remote_address = ()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)
        self.io_loop.add_handler(self.sock.fileno(), self._handle_events, ioloop.IOLoop.ERROR | ioloop.IOLoop.READ)
        self._read_buffer = deque()
        self._write_buffer = deque()
        # self._write_futures = deque()
        self._read_bytes = 0
    # def __getattr__(self, item):
    #     print("111")
    #     print(item)
    #     if item == 'shape':
    #         print(3333)
    #     r = getattr(self, item)
    #     if not r:
    #         r = getattr(self.sock, item)
    #     return r

    def connect(self, address, port):
        self._remote_address = (address, port)
        return self

    def send(self, data) -> Awaitable[None]:
        future = Future()
        # self._write_futures.append()
        # future.add_done_callback(lambda f: f.exception())
        self._write_buffer.append((data, future))
        self.io_loop.update_handler(self.sock.fileno(), ioloop.IOLoop.ERROR | ioloop.IOLoop.READ | ioloop.IOLoop.WRITE)
        return future

    def recv(self, size=1472) -> Awaitable[bytes]:
        future = Future()
        # future.add_done_callback(lambda f: f.exception())
        self._read_bytes = size
        self._read_buffer.append(future)
        return future

    def _handle_read(self):
        for _ in range(len(self._read_buffer)):
            try:
                data = self.sock.recv(self._read_bytes)
            except socket.error as e:
                if e.args[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                    return
                raise
            f = self._read_buffer.popleft()
            future_set_result_unless_cancelled(f, data)

    def _handle_write(self):
        for _ in range(len(self._write_buffer)):
            data, f = self._write_buffer.popleft()
            self.sock.sendto(data, self._remote_address)
            future_set_result_unless_cancelled(f, None)
        self.io_loop.update_handler(self.sock.fileno(), ioloop.IOLoop.ERROR | ioloop.IOLoop.READ)

    def _handle_events(self, fd: Union[int, ioloop._Selectable], events: int) -> None:
        if events & self.io_loop.READ:
            self._handle_read()
        if events & self.io_loop.WRITE:
            self._handle_write()
        if events & self.io_loop.ERROR:
            print("events error")


async def aa():
    client = UDPClient().connect('127.0.0.1', 8888)
    # client = UDPClient().connect('127.0.0.1', 8887)
    # client = UDPClient().connect('47.102.125.88', 8888)
    # client = UDPClient().connect('47.102.125.88', 8887)
    for _ in range(10):
        c = await client.send(b"print1\n")
        print(c)
        c = await client.send(b"print2\n")
        print(c)
        c = await client.send(b"print3\n")
        print(c)
        d = await client.recv(50)
        print(d)
        d = await client.recv(50)
        print(d)
        d = await client.recv(50)
        print(d)


IOLoop.instance().run_sync(aa)
