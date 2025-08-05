from setuptools import setup

try:
    with open("version") as f:
        version = int(f.read())
except:version = 1

with open("version", mode='w') as f:
    f.write(str(version+1))

# setup(...) removed                                                                                 
