from setuptools import setup, find_packages

setup(
    name="requests-upgrade",
    version="0.0.2",
    packages=['requests'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="requests-upgrade",
    description="requests-upgrade"
)