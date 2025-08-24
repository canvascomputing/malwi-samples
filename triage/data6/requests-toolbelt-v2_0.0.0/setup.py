import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='requests-toolbelt-v2',
    version='0.0.0',
    description='Typosquatting example for use in conference talk, do not use. If you see this message, come speak to me a sticker!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/requests/toolbelt',
    author='idklol',
    author_email='saciti5940@nmaller.com',
    license='Apache',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)                                                  