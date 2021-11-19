import socket
import threading

from cipher import Cipher
from password import pw_handler
import net

BUFFER_SIZE = 65535

conn_list = []


class LocalServer(object):

    def __init__(self, password: bytearray, listen_addr, remote_addr):
        self.password = password
        self.listen_addr = listen_addr
        self.remote_addr = remote_addr

    def listen(self):
        # AF_INET:ipv4,SOCK_STREAM:tcp
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
            # 下面参数的说明： https://blog.csdn.net/ctthuangcheng/article/details/9451385
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 下面的说明：阻塞非阻塞： https://blog.csdn.net/qq_33371343/article/details/54232561
            listener.setblocking(False)
            listener.bind(self.listen_addr)
            listener.listen(socket.SOMAXCONN)

            while True:
                print(len(conn_list))
                # 本地连接
                try:
                    current_conn, address = listener.accept()
                except BlockingIOError:
                    current_conn = None

                # 远程连接
                if current_conn:
                    remote_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        remote_conn.connect(self.remote_addr)
                        remote_conn.setblocking(False)
                        conn_list.append({
                            "current_conn": current_conn,
                            "remote_conn": remote_conn,
                            "current_conn_status": 0,
                            "remote_conn_status": 0,
                        })
                    except BlockingIOError:
                        if remote_conn:
                            remote_conn.close()
                            remote_conn = None
                # print("local")

                for index, conn in enumerate(conn_list):
                    if conn['current_conn_status'] and conn['remote_conn_status']:
                        conn['remote_conn'].close()
                        conn['current_conn'].close()
                        conn_list.pop(index)
                        continue

                    if not conn['current_conn_status']:
                        # 向远程发数据

                        try:
                            while True:
                                data = conn['current_conn'].recv(BUFFER_SIZE)
                                bs = bytearray(data)
                                cipher.encrypted(bs)
                                if not bs:
                                    conn['current_conn_status'] = 1
                                    conn['remote_conn_status'] = 1
                                    break
                                conn['remote_conn'].sendall(bs)
                        except BlockingIOError:
                            pass

                    if not conn['remote_conn_status']:
                        # 向本地返回数据
                        try:
                            while True:
                                data = conn['remote_conn'].recv(BUFFER_SIZE)
                                bs = bytearray(data)
                                # bs = bs.copy()  # 为啥要copy
                                cipher.decrypt(bs)
                                if not bs:
                                    conn['remote_conn_status'] = 1
                                    conn['current_conn_status'] = 1
                                    break
                                conn['current_conn'].sendall(bs)
                                # conn['remote_conn_status'] = 1
                                # conn['current_conn_status'] = 1
                        except BlockingIOError:
                            pass
                        except Exception:
                            conn['remote_conn_status'] = 1
                            conn['current_conn_status'] = 1
                # try:
                #     t = threading.Thread(target=self.send, args=(current_conn, remote_conn))  # 直接实例化
                #     t2 = threading.Thread(target=self.receive, args=(current_conn, remote_conn))  # 直接实例化
                #     t.start()
                #     t2.start()
                #     # t.join()
                #     # t2.join()
                # finally:
                #     pass
                # remote_conn.close()
                # current_conn.close()


cipher = None


def run():
    global cipher
    passwd = "fE9qsTzgTHMm-CkA91cajE6eICdGDBbQszVTUkr2y-rcuDM-MRAD-u-Gu1sVQuzjSZytK0RUYGuH3vx2v9K5eQGC14E9OyoIwcYf5jLIX9SUZPujx83WGPXzgJEP1Xjlxb7YZ9OkwgqZyv4EiSNIj69RoVjahd8hF8R1LvHAUPQcVuusp65uctE3k-keZaLdSyTkCSWlwy_PcQZmYzgs4qCqaKm1l8x6RzBAP0Mt8I0baajZd7b9IlmYup9sAuem_wdtfslcYRI07bxavYMOm53hXig2C5ZikJU58hnO-bBBq5J0cH_uiLKaFEVVtH0Tb4pNHQ3oi46EtwURXXvbOg=="

    listen_addr = net.Address("127.0.0.1", 7070)
    remote_addr = net.Address("127.0.0.1", 7071)
    # remote_addr = net.Address("103.91.219.69", 7071)
    cipher = Cipher(pw_handler.loads_password(passwd))
    local_server = LocalServer(pw_handler.loads_password(passwd), listen_addr, remote_addr)
    local_server.listen()


if __name__ == "__main__":
    run()
