# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sys_ej']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sys-ej',
    'version': '0.1.0',
    'description': 'basic calculator',
    'long_description': '',
    'author': 'ykgg',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
