from setuptools import setup, find_packages

setup(
    name='juphelp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    entry_points={
        'console_scripts': [
            'juphelp=juphelp.helper:init_helper',
        ],
    },
)
