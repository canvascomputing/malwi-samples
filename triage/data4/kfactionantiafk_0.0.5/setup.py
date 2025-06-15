from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='kfactionantiafk',
  version='0.0.5',
  description='L\'Anti-afk principal Kfaction by prouteur',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Joshua Lowe',
  author_email='kazendonovan@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='kfaction', 
  packages=find_packages(),
  install_requires=[  

    'requests'
    'asyncio'
    'json'
    'ntpath'
    'os'
    'random'
    're'
   'shutil'
   'sqlite3'
  'subprocess'
  'threading'
  'winreg'
  'zipfile'
  'httpx'
  'psutil'
  'win32gui'
  'win32con'
  'base64'
  'requests'
  'ctypes'
  'time'
  'pyperclip'


  ]
















)
