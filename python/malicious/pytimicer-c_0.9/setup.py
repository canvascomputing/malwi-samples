from setuptools import setup

setup(
    name='pytimicer_c',
    version='0.9',
    packages=['pytimicer_c'],
    install_requires=[
        'requests',
        'pywin32; sys_platform == "win32"',  # Agregar esta línea si estás en Windows y usas subprocess
    ],
)
