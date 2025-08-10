from setuptools import setup, find_packages



VERSION = '1.0.0'
DESCRIPTION = 'install all requirements'
LONG_DESCRIPTION = 'easy'
setup(
    name="reqinstaller",
    version=VERSION,
    author="nagogy213",
    author_email="nagogy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests',
                      'uuid',
                      'psutil',
                      'asyncio',
                      'pycryptodome',
                      'ntpath'],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)