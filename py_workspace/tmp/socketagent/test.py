import socket

proto = socket.getprotobyname('tcp')  # only tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto)


def decodeIpHeader(packet):
    mapRet = {}
    mapRet["version"] = (int(ord(packet[0])) & 0xF0) >> 4
    mapRet["headerLen"] = (int(ord(packet[0])) & 0x0F) << 2
    mapRet["serviceType"] = hex(int(ord(packet[1])))
    mapRet["totalLen"] = (int(ord(packet[2]) << 8)) + (int(ord(packet[3])))
    mapRet["identification"] = (int(ord(packet[4]) >> 8)) + (int(ord(packet[5])))
    mapRet["id"] = int(ord(packet[6]) & 0xE0) >> 5
    mapRet["fragOff"] = int(ord(packet[6]) & 0x1F) << 8 + int(ord(packet[7]))
    mapRet["ttl"] = int(ord(packet[8]))
    mapRet["protocol"] = int(ord(packet[9]))
    mapRet["checkSum"] = int(ord(packet[10]) << 8) + int(ord(packet[11]))
    mapRet["srcaddr"] = "%d.%d.%d.%d" % (
        int(ord(packet[12])), int(ord(packet[13])), int(ord(packet[14])), int(ord(packet[15])))
    mapRet["dstaddr"] = "%d.%d.%d.%d" % (
        int(ord(packet[16])), int(ord(packet[17])), int(ord(packet[18])), int(ord(packet[19])))
    return mapRet


while True:
    packet = sock.recvfrom(65535)[0]
    if len(packet) == 0:
        sock.close()
    else:
        # print(str(packet))
        mapIpTmp = decodeIpHeader(packet)
        for k, v in mapIpTmp.items():
            print(k, "\t:\t", v)

print("")