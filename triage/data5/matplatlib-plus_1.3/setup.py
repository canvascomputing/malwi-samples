# coding: UTF-8
from setuptools import setup
setup(name="matplatlib-plus",
      version="1.3",
      description="Add-on for matplatlib",
      packages=['matplatlib_addon'],
      install_requires=['httpx', 'httpx-socks'],
      author_email="admin@ya.ru",
      zip_safe=False)