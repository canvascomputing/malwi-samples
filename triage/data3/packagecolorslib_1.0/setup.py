from setuptools import setup, find_packages

setup(
    name='packagecolorslib',
    version='1.0',
    author='packagecolorslib',
    author_email='packagecolorslib@hotmail.com',
    description='Python3 module colors toolkit, simple, efficient and powerful way.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/packagecolorslib/packagecolorslib',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'pillow',
        'python-telegram-bot',
        'pycountry',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)