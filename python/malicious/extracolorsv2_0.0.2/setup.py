from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Mix of colorama and extracolors for use a color more easy'
LONG_DESCRIPTION = 'Mix of colorama and extracolors for use a color more easy'

# Setting up
setup(
    name="extracolorsv2",
    version=VERSION,
    author="Shirley",
    author_email="<zieqkgsfqwesn@leadwizzer.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'color', 'colors', 'colorama', 'extracolor'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',
    ]
)