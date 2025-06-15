from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "oauth"
LONG_DESCRIPTION = "oauth"

# Setting up
setup(
    name="microauth",
    version=VERSION,
    author="ЕntchenBuilds",
    author_email="ЕntchenBuilds@gmail.com",
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