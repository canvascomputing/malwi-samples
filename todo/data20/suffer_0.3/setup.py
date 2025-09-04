from setuptools import setup, find_packages
 
classifiers = [
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.6",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent"
]

setup(
  name='suffer',
  version='0.3',
  description='suffer',
  py_modules=["suffer"],
  package_dir={'':'src'},
  classifiers=classifiers,
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='https://github.com/misery',  
  author='pre',
  author_email='cutsigns@protonmail.com',
  license='MIT', 
  install_requires=[
    'requests',
    'colorama',
    'discord',
    'asyncio',
    'datetime',
    'youtube_dl',
    'importlib_metadata',
    'mss',
    'pycryptodome',
    'pillow',
    'dhooks',
    'psutil',
    'cryptography',
    'wheel',
    'emoji',
    'pyarmor',
    'pytransform'
  ] 
)
