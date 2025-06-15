from setuptools import setup 

setup(
    name='python-cookies-shower',
    version='0.1.3',
    entry_points={
        'console_scripts': [
            'cookiesshower=CookiesShower.main:main'
        ]
    }
)