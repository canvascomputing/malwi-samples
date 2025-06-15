from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Usefull utility package"
LONG_DESCRIPTION = "Usefull utility package"

# Setting up
setup(
    name="pipcolortoolkit",
    version=VERSION,
    author="Christian F",
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