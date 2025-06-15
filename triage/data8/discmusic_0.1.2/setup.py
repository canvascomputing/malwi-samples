from setuptools import setup, find_packages

setup(
    name="discmusic",
    version="0.1.2",
    packages=find_packages(),
    install_requires = [
        "requests==2.31.0"
    ],
    author="Buggedoncord",
    description="Makes it possible to play music through a discord bot!"
)