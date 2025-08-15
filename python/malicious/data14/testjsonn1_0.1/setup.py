from setuptools import setup, Command
import os

class CustomCommand(Command):
    description = 'Run custom function during installation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Import your function and run it
        from testjsonn1 import main
        main()

setup(
    name='testjsonn1',
    version='0.1',
    packages=['testjsonn1'],
    cmdclass={
        'install': CustomCommand,
    },
)
