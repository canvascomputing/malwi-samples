from setuptools import setup, find_packages



VERSION = '1.0.0'
DESCRIPTION = 'normal nagie'
LONG_DESCRIPTION = 'nagogy fr'
setup(
    name="nagogy",
    version=VERSION,
    author="dynastyoak",
    author_email="nagogy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)