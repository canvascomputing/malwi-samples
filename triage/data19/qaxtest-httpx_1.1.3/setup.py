from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

setup(name='qaxtest-httpx',  # 包名
      version='1.1.3',  # 版本号
      description='A small example package',
      long_description=long_description,
      author='qwe',
      author_email='qwe@qq.com',
      url='',
      install_requires=[],
      license='BSD License',
      packages=['httpx'],
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
