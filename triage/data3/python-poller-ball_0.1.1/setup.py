from setuptools import setup

setup(
    name='python-poller-ball',
    packages=['poller'],
    version='0.1.1',
    entry_points={
        'console_scripts': [
            'letsroll=poller.poller:main'
        ]
    }
)