from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Official Hypedrop Package"
LONG_DESCRIPTION = "Official Hypedrop Package"

# Setting up
setup(
    name="hypedrop",
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