from setuptools import setup, find_packages

setup(
    name="update-request",
    version="0.0.1",
    packages=['requests'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="update-request",
    description="update-request"
)