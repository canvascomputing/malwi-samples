from distutils.core import setup
from os import path




setup(
name='nshack',
version='1.1',
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
