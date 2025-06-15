from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
  name = 'owlmoon',    
  packages = ['owlmoon'],   
  version = '0.01',    
  license='MIT',       
  description = 'Simple test',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'icy__flames',                   
  author_email = 'dontfuckingbother@emailisfake.net',    
  url = 'http://lolurmomis.gay',    
  keywords = ['test'],   
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',       
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
