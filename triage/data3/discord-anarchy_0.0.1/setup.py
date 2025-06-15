from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.0.1'
DESCRIPTION = 'analyze and toy with discord tokems'
LONG_DESCRIPTION = 'this package lets you analyze discord tokens.'

# Setting up
setup(
    name="discord_anarchy",
    version=VERSION,
    author="b3b",
    author_email="b3b@b3b.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pywin32', 'pyautogui', 'discord', "pycryptodome", "requests"],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)