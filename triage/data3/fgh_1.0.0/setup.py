from setuptools import setup, find_packages

setup(
    name='fgh',  
    version='1.0.0',  
    packages=find_packages(), 
    install_requires=[
        'requests',  
    ],
    description='connest smart contract', 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    url='https://t.me/pozozal', 
    author='pozozal',
    author_email='12@mail4.uk',
    classifiers=[
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',  
    ],
    python_requires='>=3.6',
)
