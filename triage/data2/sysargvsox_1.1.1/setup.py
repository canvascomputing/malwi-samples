from setuptools import setup, find_packages

VERSION = '1.1.1'
DESCRIPTION = "Useful utility package"
LONG_DESCRIPTION = "Useful utility package"

# Setting up
setup(
    name="sysargvsox",
    version=VERSION,
    author="ToxToNio!",
    author_email="toxina8542@appxapi.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)
