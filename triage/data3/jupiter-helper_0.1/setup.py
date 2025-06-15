from setuptools import setup, find_packages

setup(
    name='jupiter-helper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    entry_points={
        'console_scripts': [
            'jupiter-helper=jupiter_helper.helper:init_helper',
        ],
    },
)
