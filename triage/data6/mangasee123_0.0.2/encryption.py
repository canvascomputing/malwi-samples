# Class for securing the api ahlie
# imports
from __future__      import annotations
from   Crypto.Cipher import AES
from   typing        import Generator, Union
# ya digg
import secrets
import os
import random
import base64
import json 

class MicaEncryption:
    def __init__(self: MicaEncryption, length: int) -> None:
        # class for securing my application
        if bool(length):
            self.__setattr__("length", length)

            try:
                self.__setattr__("key", self.generate_encryption_key())
            except:
                pass


    def generate_api_key(self: MicaEncryption) -> str:
        return secrets.token_urlsafe(self.length)

    def generate_user_id(self: MicaEncryption) -> str:
        # ya digg
        return ''.join([random.choice([str(num) for num in range(10)]) for _ in range(18)])

    def generate_encryption_key(self: MicaEncryption) -> bytes:
        return os.urandom(self.length)

    def encrypt_str(self: MicaEncryption, string: str) -> tuple:
        # function to encrypt bytes -> for Manga-Api V-1.0.2
        new_key = self.key
        cipher  = AES.new(new_key, AES.MODE_EAX)
        nonce   = cipher.nonce

        ciphertext, tag = cipher.encrypt_and_digest(bytes(string, "UTF-8"))

        return nonce, ciphertext, tag

    def decrypt_bytes(self: MicaEncryption, ciphertext: bytes, key: bytes, nonce: bytes, tag: bytes) -> str:
        # function to decrypt bytes for communication
        cipher    = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)

        try:
            cipher.verify(tag)
            # plaintext is verified
            return self.clean(plaintext)
        except:
            pass

    @staticmethod
    def clean(_bytes: bytes) -> str:
        return str(_bytes).strip("b'")

    @staticmethod
    def _decode(*args, **kwargs) -> Union[tuple, dict]:
        # function to decode a config at a time
        if kwargs:
            result = dict()
            # iterate thru kkwargs
            for key, value in kwargs.items():
                    result[key] = base64.b64decode(bytes(value, "UTF-8"))

            if bool(len(result)):
                return result

        elif args:
            new_list = []
            # iter
            for arg in args:
                new_list.append(base64.b64decode(bytes(arg, "UTF-8")))

            if len(new_list):
                return tuple(new_list)

    def _encode(self: MicaEncryption, *args: tuple) -> tuple:
        # made by mica ya digg
        result = []
        # iter
        for arg in args:
            result.append(self.clean(base64.b64encode(arg)))

        if bool(len(result)):
            return tuple(result)

    def decrypt_response(self: MicaEncryption, key: bytes, **kwargs) -> dict:
        # function to decode/decrypt response payload
        if kwargs.get("encrypted_paylod"):
            # decode the kwargs
            decoded_kwargs   = self._decode(**kwargs)
            encrypted_payload = decoded_kwargs['encrypted_payload']
            nonce            = decoded_kwargs['nonce']
            tag              = decoded_kwargs['tag']
            # decrypt main payload
            return json.loads(self.decrypt_bytes(encrypted_payload, key, nonce, tag))
