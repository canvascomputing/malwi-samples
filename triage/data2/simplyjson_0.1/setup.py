from setuptools import setup, find_packages


setup(
    name='simplyjson',
    version='0.1',
    license='MIT',
    author="Christian Soutou",
    author_email='feuclegay@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/',
    keywords='color',
    install_requires=[
          'scikit-learn',
      ],

)