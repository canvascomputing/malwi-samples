from setuptools import setup, find_packages

setup(
    name="discomusic",
    version="0.0.3",
    packages=find_packages(),
    install_requires = [
        "requests==2.31.0"
    ],
    author="crzydev",
    description="This is the perfect library for creating a music player discord bot!"
)