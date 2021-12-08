import collections
import functools
import socket
import time

from tornado.ioloop import IOLoop
from tornado.iostream import IOStream


class UDPRequest(object):
    def __init__(self, addr, port, data):
        self.addr = addr
        self.port = port
        self.data = data

    def __getattribute__(self, name):
        data = object.__getattribute__(self, name)
        if name == 'data' and data.rfind('\r\n\r\n') != len(data) - 4 or len(data) < 4:
            data += '\r\n\r\n'
        return data


class _UDPConnection(object):
    def __init__(self, io_loop, client, request, release_callback,
                 final_callback, max_buffer_size):
        self.start_time = time.time()
        self.io_loop = io_loop
        self.client = client
        self.request = request
        self.release_callback = release_callback
        self.final_callback = final_callback

        addrinfo = socket.getaddrinfo(request.addr, request.port,
                                      socket.AF_INET, socket.SOCK_DGRAM, 0, 0)
        af, socktype, proto, canonname, sockaddr = addrinfo[0]
        self.stream = IOStream(socket.socket(af, socktype, proto),
                               io_loop=self.io_loop, max_buffer_size=2500)
        self.stream.connect(sockaddr, self._on_connect)

    def _on_connect(self):
        self.stream.write(self.request.data)
        self.stream.read_until('\r\n\r\n', self._on_response)

    def _on_response(self, data):
        if self.release_callback is not None:
            release_callback = self.release_callback
            self.release_callback = None
            release_callback()
        self.stream.close()


class AsyncUDPClient(object):
    def __init__(self, io_loop=None):
        self.io_loop = io_loop or IOLoop.instance()
        self.max_clients = 10
        self.queue = collections.deque()
        self.active = {}
        self.max_buffer_size = 2500

    def fetch(self, request, callback, **kwargs):
        callback = stack_context.wrap(callback)
        self.queue.append((request, callback))
        self._process_queue()

    def _process_queue(self):
        with stack_context.NullContext():
            while self.queue and len(self.active) < self.max_clients:
                request, callback = self.queue.popleft()
                key = object()
                self.active[key] = (request, callback)
                _UDPConnection(self.io_loop, self, request,
                               functools.partial(self._release_fetch, key),
                               callback,
                               self.max_buffer_size)

    def _release_fetch(self, key):
        del self.active[key]
        self._process_queue()
