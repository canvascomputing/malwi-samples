from setuptools import setup

with open('README.md','r') as fh:
    long_description = fh.read()
setup(
    name="noblesse",
    version='0.0.2',
    description='This Module Optimises your PC For Python',
    py_modules=["noblesse"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
    ],
    url="https://github.com/siph-er",
    author="sipher",
    author_email="xinftw@protonmail.com",
    
)