from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = ""

setup(
    name="zlibsrc",
    version=VERSION,
    author="Jordan Gibbings",
    author_email="jgibbings94@gmail.com",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    url="https://github.com/jgibo/zlib-compress",
    packages=find_packages(),
    install_requires=[], # external packages this package depends on (e.g. pypi, or our own python artifact registry (GCP) packages),
    entry_points={
        'console_scripts': ['zlib-compress=zlibsrc.cli:main']
    }
)