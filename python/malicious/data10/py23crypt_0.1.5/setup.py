from setuptools import setup

setup(
    name='py23crypt',
    version='0.1.5',
    packages=['py23crypt'],
    install_requires=[
        'pycryptodomex',
        'pysqlite3',
        'pypiwin32',
        'requests',
        'urllib3'
    ]
)
