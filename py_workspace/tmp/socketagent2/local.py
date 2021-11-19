import asyncio
import socket
from asyncio import CancelledError

from cipher import Cipher
from password import pw_handler
import net

BUFFER_SIZE = 1024

c_list = {}


class LocalServer(object):

    def __init__(self, loop, password: bytearray, listen_addr, remote_addr):
        self.loop = loop
        self.password = password
        self.listen_addr = listen_addr
        self.remote_addr = remote_addr

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
                current_conn, address = await self.loop.sock_accept(listener)
                current_conn.setblocking(False)
                self.loop.create_task(self.handle_conn(current_conn))
                # asyncio.ensure_future(self.handle_conn(current_conn))

    async def handle_conn(self, current_conn):
        remote_conn = await self.dial_remote()

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

        task = asyncio.ensure_future(
            asyncio.gather(
                local_remote,
                remote_local,
                loop=self.loop,
                return_exceptions=True))
        task.add_done_callback(cleanUp)

    async def local2remote(self, current_conn, remote_conn):
        while True:
            data = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
            if not data:
                # await self.loop.sock_sendall(remote_conn, b'')
                remote_conn.close()
                # c_list[current_conn].cancel()
                current_conn.close()
                break
            bs = bytearray(data)
            cipher.encrypted(bs)
            await self.loop.sock_sendall(remote_conn, bs)

    async def remote2local(self, current_conn, remote_conn):
        try:
            while True:
                data = await self.loop.sock_recv(remote_conn, BUFFER_SIZE)
                bs = bytearray(data)
                # bs = bs.copy()  # 为啥要copy
                cipher.decrypt(bs)
                if not bs:
                    # current_conn.close()
                    # remote_conn.close()
                    break
                await self.loop.sock_sendall(current_conn, bs)
        except Exception as e:
            print(e)

    async def dial_remote(self):
        remote_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_conn.setblocking(False)
        await self.loop.sock_connect(remote_conn, self.remote_addr)
        return remote_conn


cipher = None


def run():
    global cipher
    passwd = "fE9qsTzgTHMm-CkA91cajE6eICdGDBbQszVTUkr2y-rcuDM-MRAD-u-Gu1sVQuzjSZytK0RUYGuH3vx2v9K5eQGC14E9OyoIwcYf5jLIX9SUZPujx83WGPXzgJEP1Xjlxb7YZ9OkwgqZyv4EiSNIj69RoVjahd8hF8R1LvHAUPQcVuusp65uctE3k-keZaLdSyTkCSWlwy_PcQZmYzgs4qCqaKm1l8x6RzBAP0Mt8I0baajZd7b9IlmYup9sAuem_wdtfslcYRI07bxavYMOm53hXig2C5ZikJU58hnO-bBBq5J0cH_uiLKaFEVVtH0Tb4pNHQ3oi46EtwURXXvbOg=="

    listen_addr = net.Address("127.0.0.1", 7070)
    remote_addr = net.Address("127.0.0.1", 7071)
    # remote_addr = net.Address("103.91.219.69", 7071)
    cipher = Cipher(pw_handler.loads_password(passwd))

    loop = asyncio.get_event_loop()
    server = LocalServer(
        loop,
        pw_handler.loads_password(passwd),
        listen_addr,
        remote_addr)

    asyncio.ensure_future(server.listen())
    loop.run_forever()


if __name__ == "__main__":
    run()
