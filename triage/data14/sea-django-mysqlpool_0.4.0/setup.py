from setuptools import setup, find_packages
setup(name="sea-django-mysqlpool", version="0.4.0", packages=find_packages(), install_requires=['seccache','sqlalchemy>=0.7'], description=("This package is to support creation of database connection pool"))
