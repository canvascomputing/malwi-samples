from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()



setup(
name='nshack',
version='1.0',
author='Nasir Ali',
url='https://github.com/nasirxo/nhack',
description='Python Hacking Library By Nasir Ali',
#long_description=long_description,
#long_description_content_type='text/markdown',
author_email='nasiralis1731@gmail.com',
author_url='https://facebook.com/nasir.xo',
packages=['nshack'],
scripts=[
'bin/fblogin',
'bin/fbmathbot',
'bin/fbmathcommentbot',
],
install_requires=[
'bs4',
'requests',
'faker',
'sympy',
'pyfiglet',
],
)
