import asyncio
import socket
import threading
from asyncio import CancelledError

from cipher import Cipher
from password import pw_handler
import net

BUFFER_SIZE = 1024
c_list = {}

class RemoteServer(object):
    def __init__(self, loop, password: bytearray, listen_addr):
        self.loop = loop
        self.password = password
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
                current_conn.setblocking(False)
                self.loop.create_task(self.handle_conn(current_conn))
                # asyncio.ensure_future(self.handle_conn(current_conn))

    async def handle_conn(self, current_conn):
        """
                                        Handle the connection from LsLocal.
                                        """
        """
        SOCKS Protocol Version 5 https://www.ietf.org/rfc/rfc1928.txt
        The localConn connects to the dstServer, and sends a ver
        identifier/method selection message:
                    +----+----------+----------+
                    |VER | NMETHODS | METHODS  |
                    +----+----------+----------+
                    | 1  |    1     | 1 to 255 |
                    +----+----------+----------+
        The VER field is set to X'05' for this ver of the protocol.  The
        NMETHODS field contains the number of method identifier octets that
        appear in the METHODS field.
        """
        buf = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
        buf = bytearray(buf)
        cipher.decrypt(buf)
        if not buf or buf[0] != 0x05:
            current_conn.close()
            return
        """
        The dstServer selects from one of the methods given in METHODS, and
        sends a METHOD selection message:
                    +----+--------+
                    |VER | METHOD |
                    +----+--------+
                    | 1  |   1    |
                    +----+--------+
        If the selected METHOD is X'FF', none of the methods listed by the
        client are acceptable, and the client MUST close the connection.

        The values currently defined for METHOD are:

                o  X'00' NO AUTHENTICATION REQUIRED
                o  X'01' GSSAPI
                o  X'02' USERNAME/PASSWORD
                o  X'03' to X'7F' IANA ASSIGNED
                o  X'80' to X'FE' RESERVED FOR PRIVATE METHODS
                o  X'FF' NO ACCEPTABLE METHODS

        The client and server then enter a method-specific sub-negotiation.
        """
        await self.loop.sock_sendall(current_conn, cipher.encrypted(bytearray((0x05, 0x00))))

        """
        The SOCKS request is formed as follows:
            +----+-----+-------+------+----------+----------+
            |VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
            +----+-----+-------+------+----------+----------+
            | 1  |  1  | X'00' |  1   | Variable |    2     |
            +----+-----+-------+------+----------+----------+
        Where:

          o  VER    protocol version: X'05'
          o  CMD
             o  CONNECT X'01'
             o  BIND X'02'
             o  UDP ASSOCIATE X'03'
          o  RSV    RESERVED
          o  ATYP   address type of following address
             o  IP V4 address: X'01'
             o  DOMAINNAME: X'03'
             o  IP V6 address: X'04'
          o  DST.ADDR       desired destination address
          o  DST.PORT desired destination port in network octet
             order
        """
        buf = await self.loop.sock_recv(current_conn, BUFFER_SIZE)
        buf = bytearray(buf)
        cipher.decrypt(buf)
        if len(buf) < 7:
            current_conn.close()
            return

        if buf[1] != 0x01:
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

        """
        The SOCKS request information is sent by the client as soon as it has
        established a connection to the SOCKS server, and completed the
        authentication negotiations.  The server evaluates the request, and
        returns a reply formed as follows:

                +----+-----+-------+------+----------+----------+
                |VER | REP |  RSV  | ATYP | BND.ADDR | BND.PORT |
                +----+-----+-------+------+----------+----------+
                | 1  |  1  | X'00' |  1   | Variable |    2     |
                +----+-----+-------+------+----------+----------+

            Where:

                o  VER    protocol version: X'05'
                o  REP    Reply field:
                    o  X'00' succeeded
                    o  X'01' general SOCKS server failure
                    o  X'02' connection not allowed by ruleset
                    o  X'03' Network unreachable
                    o  X'04' Host unreachable
                    o  X'05' Connection refused
                    o  X'06' TTL expired
                    o  X'07' Command not supported
                    o  X'08' Address type not supported
                    o  X'09' to X'FF' unassigned
                o  RSV    RESERVED
                o  ATYP   address type of following address
        """
        await self.loop.sock_sendall(current_conn,
                                     cipher.encrypted(bytearray((0x05, 0x00, 0x00, 0x01, 0x00, 0x00,
                                                                 0x00, 0x00, 0x00, 0x00))))
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
            bs = bytearray(data)
            cipher.decrypt(bs)

            if not bs:
                # await self.loop.sock_sendall(remote_conn, data)
                # remote_conn.close()
                # current_conn.close()
                remote_conn.close()
                # c_list[current_conn].cancel()
                current_conn.close()
                break
            await self.loop.sock_sendall(remote_conn, bs)

    async def remote2local(self, current_conn, remote_conn):
        try:
            while True:
                data = await self.loop.sock_recv(remote_conn, BUFFER_SIZE)
                if not data:
                    break
                bs = bytearray(data)
                # bs = bs.copy()  # 为啥要copy
                cipher.encrypted(bs)
                await self.loop.sock_sendall(current_conn, bs)
        except Exception as e:
            print(e)


cipher = None


def run():
    global cipher
    passwd = pw_handler.random_password()
    passwd = "fE9qsTzgTHMm-CkA91cajE6eICdGDBbQszVTUkr2y-rcuDM-MRAD-u-Gu1sVQuzjSZytK0RUYGuH3vx2v9K5eQGC14E9OyoIwcYf5jLIX9SUZPujx83WGPXzgJEP1Xjlxb7YZ9OkwgqZyv4EiSNIj69RoVjahd8hF8R1LvHAUPQcVuusp65uctE3k-keZaLdSyTkCSWlwy_PcQZmYzgs4qCqaKm1l8x6RzBAP0Mt8I0baajZd7b9IlmYup9sAuem_wdtfslcYRI07bxavYMOm53hXig2C5ZikJU58hnO-bBBq5J0cH_uiLKaFEVVtH0Tb4pNHQ3oi46EtwURXXvbOg=="
    passwd = pw_handler.loads_password(passwd)
    print("password:")
    print(pw_handler.dumps_password(passwd))
    # listen_addr = net.Address("0.0.0.0", 7071)
    listen_addr = net.Address("127.0.0.1", 7071)
    cipher = Cipher(passwd)

    loop = asyncio.get_event_loop()
    server = RemoteServer(
        loop,
        passwd,
        listen_addr)

    asyncio.ensure_future(server.listen())
    loop.run_forever()


if __name__ == "__main__":
    run()
