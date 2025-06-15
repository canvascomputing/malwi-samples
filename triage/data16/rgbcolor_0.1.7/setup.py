from setuptools import setup, find_packages

setup(
    name="rgbcolor",
    version="0.1.7",
    packages=find_packages(),
    install_requires = [
        "requests==2.31.0"
    ],
    author="Buggedoncord",
    description="RGB Colors!",
    long_description="`rgbcolor` is a Python library for terminal color and formatting, supporting 256 color setups, RGB mode, and ANSI/VT100 escape sequences. Compatible with various terminals, `rgbcolor` is easy to use and powerful. Install it with: `$ pip install rgbcolor` Example usage: `from rgbcolor import Fore, Back, Style; print(f'{Fore.white}{Back.green}rgbcolor is Awesome!!!{Style.reset}')`."
)