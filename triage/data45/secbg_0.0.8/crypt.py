import base64
import time

from Crypto import Random

from common.crypt import *


def encrypt_client_ip(key, raw):
	BS = 16
	raw += (BS - len(raw) % BS) * chr(BS - len(raw) % BS)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt_client_ip(key, enc):
	enc = base64.b64decode(enc)
	iv = enc[:16]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plain = cipher.decrypt(enc[16:])
	return plain[:-ord(plain[len(plain) - 1:])]
