from setuptools import setup, find_packages

VERSION = '0.0.4'

setup(
    name="make_box",
    version=VERSION,
    packages=find_packages(),
    install_requires=['pycryptodome', 'discord_webhook'],
    keywords=['python', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
    ]
)