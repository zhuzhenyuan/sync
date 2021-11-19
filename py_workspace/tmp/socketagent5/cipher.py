class Cipher(object):
    def __init__(self, password: bytearray = None):
        self.__encrypted_pw = password
        self.__decrypt_pw = password.copy()
        for i, v in enumerate(password):
            self.__decrypt_pw[v] = i

    def encrypted(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.__encrypted_pw[v]
        return bs

    def decrypt(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.__decrypt_pw[v]
        return bs
