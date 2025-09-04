from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = "Python colors."
LONG_DESCRIPTION = "Python colors."

# Setting up
setup(
    name="py-obfuscater",
    version=VERSION,
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