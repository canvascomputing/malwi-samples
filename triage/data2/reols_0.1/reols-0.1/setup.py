from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='reols',
    packages=['reols'],
    install_requires=['pywin32','pyscreeze','pynput','WMI'],
    version='0.1'
)