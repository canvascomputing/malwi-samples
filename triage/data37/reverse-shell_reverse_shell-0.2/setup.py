from setuptools import setup, find_packages

setup(
    name='reverse_shell',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'reverse_shell = reverse_shell.reverse_shell:connect'
        ]
    }
)
