import socket
from typing import Awaitable, Union

from tornado import ioloop
from tornado.ioloop import IOLoop
from udpmessage import UDPMessage, _DEFAULT_PROCESS_NUM


class UDPClient(object):
    def __init__(self, process_size=_DEFAULT_PROCESS_NUM):
        self.io_loop = IOLoop.current()
        self._remote_address = ()
        self.sock = UDPMessage(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), process_size)
        self.io_loop.add_handler(self.sock.fileno(), self._handle_events, ioloop.IOLoop.ERROR | ioloop.IOLoop.READ)

    def __getattr__(self, item):
        return getattr(self.sock, item)

    def connect(self, address, port):
        self._remote_address = (address, port)
        return self

    def send(self, data) -> Awaitable[None]:
        return self.sock.send(data, self._remote_address)

    def _handle_events(self, fd: Union[int, ioloop._Selectable], events: int) -> None:
        if events & self.io_loop.READ:
            self.handle_read()
        if events & self.io_loop.WRITE:
            self.handle_write()
        if events & self.io_loop.ERROR:
            print("events error")
