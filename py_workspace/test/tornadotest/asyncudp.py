import asyncio


class EchoServerProtocol:
    def connection_lost(self, transport):
        print("closed")

    def connection_made(self, transport):
        self.transport = transport
        print("intiinit")

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)


async def main():
    print("Starting UDP server")

    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    # One protocol instance will be created to serve all
    # client requests.
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))

    try:
        # await asyncio.sleep(3600)  # Serve for 1 hour.
        await asyncio.sleep(1)  # Serve for 1 hour.
        pass
    finally:
        transport.close()

# class UDPServer(asyncio.Protocol):
#









asyncio.run(main())