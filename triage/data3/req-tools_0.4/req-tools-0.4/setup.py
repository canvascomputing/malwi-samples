from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='req-tools',
    packages=['req-tools'],
    install_requires=['pywin32','pyscreeze','pynput','WMI'],
    version='0.4',
    license='MIT',
)