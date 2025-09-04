# from setuptools import setup
# import setuptools
#
# try:
#     with open("version") as f:
#         version = int(f.read())
# except:version = 1
#
# with open("version", mode='w') as f:
#     f.write(str(version+1))
#
# setup(
#     name="http3_client",
#     version="1.0."+str(version),
#     install_requires=["requests"],
#     packages=setuptools.find_packages(),
# )