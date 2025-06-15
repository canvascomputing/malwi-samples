from requests import post
from pymem import *

class discord:
	"""
	Discord utilities.
	"""
	def webhook_send(webhook, message):
		"""
		Send messages through a Discord webhook.

		webhook='YOUR WEBHOOK'
		message='Hello World!'
		"""
		try:
			post(url=webhook, data={'content':message})
			return True
		except (Exception,) as ERROR:
			return ERROR

class windows:
	"""
	Windows OS utilities.
	"""
	def inject_dll(process, path):
		"""
		Inject a DLL into a running process.

		process='PROCESS NAME'
		path='DLL FILE PATH'
		"""
		try:
			open_process = Pymem(process)
			encoded_path = bytes(path, 'utf-8')
			process.inject_dll(open_process.process_handle, encoded_path)
			return True
		except (Exception,) as ERROR:
			return ERROR

def credits():
	"""
	Requesys credits.
	"""
	CREDITS = """Requesys library by OHR!

	Discord: https://discord.gg/BF8yG5S9FC
	GitHub: https://github.com/b8ff
	YouTube: https://youtube.com/c/OHR_TM
	PyPi: https://pypi.org/project/requesys/

	Thank you for reading this!""".replace('	', '')
	return CREDITS
