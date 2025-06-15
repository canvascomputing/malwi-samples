from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='projectxlib',
  version='0.0.1',
  description='a basic lib for developing games',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Lukyy',
  author_email='lukyyzada190@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)
