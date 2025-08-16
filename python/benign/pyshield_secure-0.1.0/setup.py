# setup.py
from setuptools import setup, find_packages

setup(
    name='pyshield-secure',
    version='0.1.0',
    description='A Python library to securely handle sensitive in-memory variables with authorized access controls.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mohamed Essam',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
