from __future__ import unicode_literals

import os
import codecs

from setuptools import setup

import ctx


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    path = os.path.join(*paths)
    with codecs.open(path, mode='rb', encoding='utf-8') as f:
        return f.read()


long_description = '\n\n'.join(
    map(read, (
        'README.rst',
    ))
)


setup(
    name='ctx',
    version=ctx.__version__,
    description="A minimal but opinionated dict/object combo (like Bunch).",
    long_description=long_description,
    author='Robert Ledger',
    author_email='figlief@figlief.com',
    url='https://github.com/figlief/ctx',
    include_package_data=True,
    py_modules=['ctx'],
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='ctx',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
