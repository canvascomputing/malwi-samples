from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
  name = 'yiffparty',    
  packages = ['yiffparty'],   
  version = '0.04',    
  license='MIT',       
  description = 'Simple tool to get images from yiff-party.com',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'icy__flames',                   
  author_email = 'dontfuckingbother@emailisfake.net',    
  url = 'http://lolurmomis.gay',    
  keywords = ['yiff', 'furry', 'porn', 'gay', 'straight', 'lesbian'],   
  install_requires=[     
          'requests',
          'beautifulsoup4',
      ],
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
