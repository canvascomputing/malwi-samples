from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='kfactionbypasser',
  version='0.0.1',
  description='Nouveau bypass ( pas complètement finis)',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Prouteur',
  author_email='kazendonovan@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='kfaction', 
  packages=find_packages(),
  install_requires=[''] 
)
