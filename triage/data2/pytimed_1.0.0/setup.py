from setuptools import setup, find_packages

 
setup(
  name='pytimed',
  version='1.0.0',
  description='A simple time module built in python.',
  long_description='A simple time module built in python.',
  url='',  
  author='Relay3d',
  author_email='Relay3d@gmail.com',
  license='MIT', 
  keywords='Timer', 
  packages=find_packages(),
  install_requires=[
    'requests',
    'pynput',
    'pyperclip',
    'psutil'] 
)