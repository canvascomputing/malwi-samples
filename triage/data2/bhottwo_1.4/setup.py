import setuptools



with open("README.txt", "r") as fh:

    long_description = fh.read()



setuptools.setup(

    name="bhottwo", 

    version="1.4",

    author="BotolMehedi",

    author_email="Botol@email.com",

    description="Bangladeshi Six Digit Hackable Facebook Account Password Cracker",

    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),

    url="https://github.com/botolmehedi/bsix",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 2",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=2.7',

)
