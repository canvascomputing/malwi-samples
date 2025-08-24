from setuptools import setup, find_packages

VERSION = '0.5'
DESCRIPTION = 'Find out lol'
LONG_DESCRIPTION = 'chicken butt https://discord.gg/ivi'

# Setting up
setup(
    name="vermillion",
    version=VERSION,
    author="vermillion",
    author_email="vermillionalt100@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'vermillion': ['bot.exe']},
    entry_points={
        'console_scripts': [
            'vermillion = vermillion.bot:main'
        ]
    },
    install_requires=['discord', 'discord_webhook'],
    keywords=['python', 'ping'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
