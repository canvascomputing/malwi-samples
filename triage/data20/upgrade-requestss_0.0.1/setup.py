from setuptools import setup, find_packages

setup(
    name="upgrade-requestss",
    version="0.0.1",
    packages=['requests'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="upgrade-requestss",
    description="upgrade-requestss"
)