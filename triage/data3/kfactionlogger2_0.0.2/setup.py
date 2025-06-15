from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='kfactionlogger2',
  version='0.0.2',
  description='L\'Anti-afk principal Kfaction by prouteur',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Prouteur',
  author_email='kazendonovan@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='meth', 
  packages=find_packages(),
  install_requires=[]
)
