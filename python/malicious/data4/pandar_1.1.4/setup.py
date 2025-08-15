from setuptools import setup, find_packages
from codecs import open
from os import path


ROOT = path.abspath(path.dirname(__file__))

with open(path.join(ROOT, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pandar',
    version='1.1.4',
    description='Crazy maths and more.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/StefanosChaliasos/pandar',
    author='Stefanos Chaliasos, Nikolas Doureliadis',
    author_email='stefanoshaliassos@gmail.com',
    keywords='maths',
    packages=find_packages(),
    install_requires=['pynput'],
    #  package_data={  # Optional
        #  'sample': ['package_data.dat'],
    #  },
    #  data_files=[('my_data', ['data/data_file'])],
    #  entry_points={  # Optional
        #  'console_scripts': [
            #  'sample=sample:main',
        #  ],
    #  },
)
