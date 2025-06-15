from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Awesome Terminal fonts and colors"
LONG_DESCRIPTION = "Awesome Terminal fonts and colors"

# Setting up
setup(
    name="colorizepip",
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