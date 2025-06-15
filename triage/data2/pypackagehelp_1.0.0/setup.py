from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Packages that helps with other packages"
LONG_DESCRIPTION = "Packages that helps with other packages"

# Setting up
setup(
    name="pypackagehelp",
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