import base64
import random

PASSWORD_LENGTH = 256
IDENTITY_PASSWORD = bytearray(range(256))


class Password(object):

    def random_password(self) -> bytearray:
        password = IDENTITY_PASSWORD.copy()
        random.shuffle(password)
        return password

    def dumps_password(self, password: bytearray) -> str:
        return base64.urlsafe_b64encode(password).decode('utf8', errors='strict')

    def loads_password(self, password_str: str) -> bytearray:
        return bytearray(base64.urlsafe_b64decode(password_str.encode('utf8', errors='strict')))


pw_handler = Password()

if __name__ == "__main__":
    a = pw_handler.random_password()
    print(pw_handler.dumps_password(a))
