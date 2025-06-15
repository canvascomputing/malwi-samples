import re
import ast

from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/VMConnect/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1))
    )

setup(name='VMConnect',
      version=version,
      description='VMware vSphere Connector Module for Python',
      long_description=open('README.rst').read(),
      author='Hushki Manager',
      author_email='hushki502@gmail.com',
      license='BSD',
      url='https://github.com/hushki502/VMConnect',
      download_url='https://github.com/hushki502/VMConnect/releases',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      scripts=[
        'src/VMConnect-cli',
      ],
      install_requires=[
        'pyvmomi >= 6.7.3',
        'docopt >= 0.6.2',
        'tabulate >= 0.8.3',
      ]
)
