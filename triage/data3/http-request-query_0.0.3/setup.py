import setuptools

setuptools.setup(
    name="http_request_query",
    version="0.0.3",
    packages=setuptools.find_packages(),
    author="Rajesh Kanumuru",
    description="Dont install this package, purely testing purpose",
    entry_points={
        'console_scripts': [
            'http_request_query = http_query.http_query:main'
        ]
    },
    install_requires= [
        'click',
        'requests'
    ]
)