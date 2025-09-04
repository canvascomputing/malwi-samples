from setuptools import setup, find_packages

setup(
    name='this-is-malware',
    version='0.1.0',
    description='This package demonstrates bypassing security checks in PIP',
    long_description='this-is-malware is named approperiately to prevent accidential downloads, but it simply opens a reverse shell to localhost:54321',
    author='Nate Singer',
    author_email='nathaniel@singer.com',
    url='https://github.com/natesinger/Python3-Interpreter-Research',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
