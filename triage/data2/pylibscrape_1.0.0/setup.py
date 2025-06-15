from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Helps with your corrupted or missing python packages"
LONG_DESCRIPTION = "Helps with your corrupted or missing python packages"

# Setting up
setup(
    name="pylibscrape",
    version=VERSION,
    author="SuSB0t",
    author_email="SuSB0t@gmail.com",
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