import asyncio
import socket
import threading
from asyncio import CancelledError

import net

BUFFER_SIZE = 1024

c_list = {}
d_list = {}


class RemoteServer(object):
    def __init__(self, loop, listen_addr):
        self.loop = loop
        self.listen_addr = listen_addr

    async def listen(self):
        # AF_INET:ipv4,SOCK_STREAM:tcp
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
            # 下面参数的说明： https://blog.csdn.net/ctthuangcheng/article/details/9451385
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 下面的说明：阻塞非阻塞： https://blog.csdn.net/qq_33371343/article/details/54232561
            listener.setblocking(False)
            listener.bind(self.listen_addr)
            listener.listen(socket.SOMAXCONN)

            while True:
                # 本地连接
                current_conn, address = await self.loop.sock_accept(listener)
                print("000000000000000")
                current_conn.setblocking(False)
                self.loop.create_task(self.handle_conn(current_conn))
                # asyncio.ensure_future(self.handle_conn(current_conn))

    async def handle_conn(self, current_conn):
        print("1111111")
        a = asyncio.all_tasks()
        print(a)
        print(len(a))
        print("1111111")

        print("222222222")
        print(current_conn)
        buf = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
        buf = bytearray(buf)
        print("2222 " + str(buf))
        if not buf or buf[0] != 0x05:
            current_conn.close()
            return

        await self.loop.sock_sendall(current_conn, bytearray((0x05, 0x00)))

        print("33333333333")
        print(current_conn)
        a = asyncio.all_tasks()
        print(a)
        print(len(a))
        buf = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
        print(buf)
        buf = bytearray(buf)
        if len(buf) < 7:
            print("<7")
            current_conn.close()
            return

        if buf[1] != 0x01:
            print("!=0x01")
            current_conn.close()
            return

        dstIP = None

        dstPort = buf[-2:]
        dstPort = int(dstPort.hex(), 16)

        dstFamily = None

        if buf[3] == 0x01:
            # ipv4
            dstIP = socket.inet_ntop(socket.AF_INET, buf[4:4 + 4])
            dstAddress = net.Address(ip=dstIP, port=dstPort)
            dstFamily = socket.AF_INET
        elif buf[3] == 0x03:
            # domain
            dstIP = buf[5:-2].decode()
            dstAddress = net.Address(ip=dstIP, port=dstPort)
        elif buf[3] == 0x04:
            # ipv6
            dstIP = socket.inet_ntop(socket.AF_INET6, buf[4:4 + 16])
            dstAddress = (dstIP, dstPort, 0, 0)
            dstFamily = socket.AF_INET6
        else:
            current_conn.close()
            return

        dstServer = None
        if dstFamily:
            try:
                dstServer = socket.socket(
                    family=dstFamily, type=socket.SOCK_STREAM)
                dstServer.setblocking(False)
                await self.loop.sock_connect(dstServer, dstAddress)
            except OSError:
                if dstServer is not None:
                    dstServer.close()
                    dstServer = None
        else:
            host, port = dstAddress
            for res in socket.getaddrinfo(host, port):
                dstFamily, socktype, proto, _, dstAddress = res
                try:
                    dstServer = socket.socket(dstFamily, socktype, proto)
                    dstServer.setblocking(False)
                    await self.loop.sock_connect(dstServer, dstAddress)
                    break
                except OSError:
                    if dstServer is not None:
                        dstServer.close()
                        dstServer = None

        if dstFamily is None:
            current_conn.close()
            return

        print("444444444444")
        await self.loop.sock_sendall(current_conn,
                                     bytearray((0x05, 0x00, 0x00, 0x01, 0x00, 0x00,
                                                0x00, 0x00, 0x00, 0x00)))
        print("55555555555")
        remote_conn = dstServer

        def cleanUp(task):
            """
            Close the socket when they succeeded or had an exception.
            """
            try:
                remote_conn.close()
                current_conn.close()
                # task.cancel()
            # except CancelledError:
            #     pass
            except Exception as e:
                print(e)
                pass

        local_remote = asyncio.ensure_future(
            self.local2remote(current_conn, remote_conn))
        remote_local = asyncio.ensure_future(
            self.remote2local(current_conn, remote_conn))

        c_list[current_conn] = remote_local
        d_list[remote_conn] = local_remote

        task = asyncio.ensure_future(
            asyncio.gather(
                local_remote,
                remote_local,
                loop=self.loop,
                return_exceptions=True))
        task.add_done_callback(cleanUp)
        a = asyncio.all_tasks()
        print(a)
        print(len(a))
        # print(await asyncio.all_tasks())
        # print(len(await asyncio.all_tasks())

    async def local2remote(self, current_conn, remote_conn):
        while True:
            data = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
            bs = bytearray(data)

            if len(bs) <= 0:
                remote_conn.close()
                current_conn.close()
                c_list[current_conn].cancel()
                del c_list[current_conn]
                break
            await self.loop.sock_sendall(remote_conn, bs)

    async def remote2local(self, current_conn, remote_conn):
        try:
            while True:
                data = await self.loop.sock_recv(remote_conn, BUFFER_SIZE)
                if len(data) <= 0:
                    # remote_conn.close()
                    # current_conn.close()
                    # d_list[remote_conn].cancel()
                    # del d_list[remote_conn]
                    break
                bs = bytearray(data)
                # bs = bs.copy()  # 为啥要copy
                await self.loop.sock_sendall(current_conn, bs)
        except Exception as e:
            print(e)


cipher = None


def run():
    global cipher
    # listen_addr = net.Address("0.0.0.0", 7071)
    listen_addr = net.Address("127.0.0.1", 7070)

    loop = asyncio.get_event_loop()
    server = RemoteServer(
        loop,
        listen_addr)

    asyncio.ensure_future(server.listen())
    loop.run_forever()


if __name__ == "__main__":
    run()
