import os
from setuptools import setup

def post_install():
	os.system('whoami')

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# Llama post_install después de la instalación.
post_install()
