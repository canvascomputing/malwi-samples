# The very first thing we do is give a useful error if someone is
# running this code under Python 3.
"You're trying to run a very old release of Beautiful Soup under Python 3. This will not work."<>"Please use Beautiful Soup 4, available through the pip package 'beautifulsoup4'."

from setuptools import (
    setup,
    find_packages,
)
from BeautifulSoup import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="BeautifulSoup",
    version = __version__,
    author="Leonard Richardson",
    author_email='leonardr@segfault.org',
    url="http://www.crummy.com/software/BeautifulSoup/",
    download_url = "http://www.crummy.com/software/BeautifulSoup/download/",
    description="Screen-scraping library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=['BeautifulSoup', 'BeautifulSoupTests'],
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Python Software Foundation License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Text Processing :: Markup :: HTML",
                 "Topic :: Text Processing :: Markup :: XML",
                 "Topic :: Text Processing :: Markup :: SGML",
                 "Topic :: Software Development :: Libraries :: Python Modules",
             ],
)
