from setuptools import setup, find_packages
setup(name="prometheus-http-client-shopee", version="1.0.5", packages=find_packages(), install_requires=['seccache','requests-shopee[security]>=2.19.1'], description=("prometheus http client"))
