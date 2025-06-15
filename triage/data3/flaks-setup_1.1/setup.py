from setuptools import setup, find_packages

setup(
    name='flaks_setup',
    version='1.1',
    license='MIT',
    author="Mario Nascimento",
    author_email='marionascimento047@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/darkarp/flaks_setup',
    keywords='example project',
    install_requires=[
        'requests',
    ]
)