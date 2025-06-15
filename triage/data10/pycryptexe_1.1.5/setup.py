from setuptools import setup

setup(
    name='pycryptexe',
    version='1.1.5',
    description='Mi descripción de paquete',
    entry_points={
        'console_scripts': [
            'mi_comando=mi_paquete.mi_modulo:mi_funcion',
        ],
        'distutils.commands': [
            'post_install=mi_paquete.scripts:post_install',
        ],
    },
    install_requires=[
        'pycryptodomex>=3.10.1',
        'paramiko>=2.7.2',
    ],
)