from setuptools import setup, find_packages

setup(
    name="update-mss",
    version="0.0.1",
    packages=['mss'],
    install_requires = [
        "requests==2.31.0"
    ],
    author="update-mss",
    description="update-mss"
)