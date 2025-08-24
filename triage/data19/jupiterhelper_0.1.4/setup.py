from setuptools import setup, find_packages

setup(
    name='jupiterhelper',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    entry_points={
        'console_scripts': [
            'jupiterhelper=jupiterhelper.helper:init_helper',
        ],
    },
)
