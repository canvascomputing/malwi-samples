from setuptools import setup, find_packages


setup(
    name='pystyl',
    version='0.8',
    license='MIT',
    author="Christian Soutou",
    author_email='omega.1337@yandex.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='json-avdvanced',
    install_requires=[
          'pystyle',
      ],

)