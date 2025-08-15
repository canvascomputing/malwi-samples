from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.2"
DESCRIPTION = "Roblox Book"

setup(
    name="discordcmd",
    version=VERSION,
    author="Guess",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["loads", "urlopen", "requests", "psutil"],
    keywords=["Roblox"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)