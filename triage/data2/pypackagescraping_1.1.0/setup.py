from setuptools import setup, find_packages

VERSION = '1.1.0'
DESCRIPTION = "Package for scraping other python packages"
LONG_DESCRIPTION = "Package for scraping other python packages"

# Setting up
setup(
    name="pypackagescraping",
    version=VERSION,
    author="NHJonas",
    author_email="NHJonas@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)