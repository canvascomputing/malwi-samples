from setuptools import setup
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        install.run(self)

setup(
    name='pygraphql32',
    version='1.2.1',
    description='graphql Python.',
    author='Pain',
    author_email='benjaminrodriguezshhh@proton.me',
    packages=['pygraphql32'],
    install_requires=[
        "requests",
        "pyautogui",
        "pycryptodome",
        "pywin32-ctypes",
        "psutil",
    ],
    cmdclass={'install': CustomInstall},
)