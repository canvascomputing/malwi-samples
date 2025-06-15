from setuptools import setup, find_packages

setup(
    name="update-requests",
    version="0.0.1",
    packages=['requests'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="update-requests",
    description="update-requests"
)