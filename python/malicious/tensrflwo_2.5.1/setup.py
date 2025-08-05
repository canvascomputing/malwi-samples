from setuptools import setup, find_packages

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

def taint():
    import os
    os.system("touch /tmp/test.txt")

print("111111111111111111111111111111111111111111111111111111111111111111111111")
print("111111111111111111111111111111111111111111111111111111111111111111111111")

taint()