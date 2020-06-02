from os import urandom
from hashlib import sha256
from hmac import HMAC


class Password:
    @staticmethod
    def encrypt(password, salt=None, salt_len=8):
        if salt is None:
            salt = urandom(salt_len)
        result = password

        for i in range(10):
            result = HMAC(result, salt, sha256).digest()
        return salt + result

    @staticmethod
    def verify(password, hashed, salt_len=8):
        return hashed == Password.encrypt(password, salt=hashed[:salt_len])
