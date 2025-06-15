from setuptools import setup, find_packages

setup(
    name='numberpy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hello-world=reqwests.index:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple hello world package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/reqwests',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
