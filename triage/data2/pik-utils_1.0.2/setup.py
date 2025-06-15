from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = "Utils ofr pik"
LONG_DESCRIPTION = "Utils ofr pik"

# Setting up
setup(
    name="pik-utils",
    version=VERSION,
    author="GigaAlex",
    author_email="nick.faltermeier@gmx.de",
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