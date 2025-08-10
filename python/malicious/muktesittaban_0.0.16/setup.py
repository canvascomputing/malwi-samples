from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.16'
DESCRIPTION = 'MuktesiTABAN'
LONG_DESCRIPTION = 'MuktesiTABAN'

# Setting up
setup(
    name="MuktesitTABAN",
    version=VERSION,
    author="MuktesiT",
    author_email="<muktesitdijital@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['GPUtil==1.4.0','notify2','pyfiglet','Pyrogram','pyTelegramBotAPI','pytz','requests','rich','parsel'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
