from setuptools import (
    find_packages,
    setup,
)

FILE_NAME = 'VERSION'


with open(FILE_NAME) as file:
    version = file.read()

with open('requirements.txt') as file:
    requirements = file.readlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fastapi_toolkit',
    version=version,
    description='Package for creating web app using fastapi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/timaakulich/fastapi_toolkit',
    author='Timofey Akulich',
    author_email='tima.akulich@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'fastapi-toolkit = fastapi_toolkit.console_scripts:main'
        ]
    },
)
