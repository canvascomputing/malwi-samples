import platform
from setuptools import setup


# Ubuntu: sudo apt install espeak ffmpeg
install_requires = [
    'comtypes; platform_system == "Windows"',
    'pypiwin32; platform_system == "Windows"',
    'pywin32; platform_system == "Windows"',
    'pyobjc>=2.4; platform_system == "Darwin"'
]


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='pytspeak',
    packages=['pytspeak', 'pytspeak.drivers'],
    version='3.23',
   description='pytspeak is a library for text-to-speech conversion in Python.',
    long_description=long_description,
    summary='Convert Text To Speech for Python',
    author='Nine Mbhat',
    url='https://github.com/nateshmbhat/pytspeak',
    author_email='ninembhat@outlook.com',
    install_requires=install_requires ,
    keywords=['text','speach'],
    classifiers = [
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
    ],
)
