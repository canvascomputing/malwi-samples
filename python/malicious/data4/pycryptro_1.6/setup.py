from setuptools import setup, find_packages


setup(
    name='pycryptro',
    version='1.6',
    license='MIT',
    author="unknownwhoami",
    author_email='claysmith@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/findme',
    keywords='crypter project',
    install_requires=[
          'requests',
      ],

)
