from setuptools import setup, find_packages
import codecs
import os


DESCRIPTION = 'Python Crypter For Red Teaming'

# Setting up
setup(
    name="pycrypte",
    author="whoami (claysmith)",
    author_email="<claysmith@yahoo.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['termcolor', 'requests', 'randoms'],
    keywords=['python', 'crypter', 'avbypass', 'crypt'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)
