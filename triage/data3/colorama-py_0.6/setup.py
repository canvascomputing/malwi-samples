from setuptools import setup, find_packages


setup(
    name='colorama-py',
    version='0.6',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='email@example.com',
    packages=find_packages('colorama-py'),
    package_dir={'': 'colorama-py'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
