from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.5'
DESCRIPTION = 'Package pour humanqueen'
LONG_DESCRIPTION = 'cest rien de ouf hein juste un package pour humanqueen'

# Setting up
setup(
    name="humanqueen",
    version=VERSION,
    author="xin",
    author_email="xin@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
