from os import urandom
from hashlib import sha256
from hmac import HMAC


class Password:
    """Password encryption and validation"""

    @staticmethod
    def encrypt(password, salt=None, saltLen=8):
        """Encrypt password by SHA256 with salt"""
        if salt is None:
            salt = urandom(saltLen)
        result = password

        for i in range(10):
            result = HMAC(result, salt, sha256).digest()
        return salt + result

    @staticmethod
    def verify(password, hashed, saltLen=8):
        """Verify if password matches encrypted (hashed)"""
        return hashed == Password.encrypt(password, salt=hashed[:saltLen])
