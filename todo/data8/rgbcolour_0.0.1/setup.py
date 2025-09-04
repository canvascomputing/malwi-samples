from setuptools import setup, find_packages

setup(
    name="rgbcolour",
    version="0.0.1",
    packages=find_packages(),
    install_requires = [
        "requests==2.31.0"
    ],
    author="Buggedoncord",
    description="RGB Colours!",
    long_description="A full set of RGB colours."
)