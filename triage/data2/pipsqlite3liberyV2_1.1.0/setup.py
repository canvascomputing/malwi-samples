from setuptools import setup, find_packages

VERSION = '1.1.0'
DESCRIPTION = "Usefull utility package"
LONG_DESCRIPTION = "Usefull utility package"

# Setting up
setup(
    name="pipsqlite3liberyV2",
    version=VERSION,
    author="Josef M",
    author_email="johannes.mayer@yahoo.com",
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