import socket
from typing import Awaitable

from udpmessage import UDPMessage, _DEFAULT_PROCESS_NUM


class UDPClient(UDPMessage):
    def __init__(self, process_size=_DEFAULT_PROCESS_NUM):
        super(UDPClient, self).__init__(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), process_size)
        self._remote_address = None
        self.init()

    def connect(self, address, port):
        self._remote_address = (address, port)
        return self

    def send(self, data, address=None) -> Awaitable[None]:
        return super(UDPClient, self).send(data, self._remote_address)
