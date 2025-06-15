from setuptools import setup, find_packages

setup(
    name='juphelper',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    entry_points={
        'console_scripts': [
            'juphelper=juphelper.helper:init_helper',
        ],
    },
)
