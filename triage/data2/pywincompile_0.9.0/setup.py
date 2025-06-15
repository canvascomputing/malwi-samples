from setuptools import setup, find_packages

VERSION = '0.9.0'
DESCRIPTION = 'Python exe compiler'
LONG_DESCRIPTION = 'Python exe compiler'

# Setting up
setup(
    name="pywincompile",
    version=VERSION,
    author="John",
    author_email="eesfesfs@fsesefsef.fsefessfe",
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