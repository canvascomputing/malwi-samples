from setuptools import setup, find_packages
#MAO2116
setup(
    name='SIAMTTVIEWS',
    packages=find_packages(),
    include_package_data=True,
    version="5.1.1",
    description='A Advance Phishing Tool Made By Siam Rahman',
    author='SIAM RAHMAN',
    author_email='s14mbro1@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['lolcat','requests','bs4','rich'],
 
    keywords=['siambomber', 'siamphisher', 'SiamRahman', 'Haxorsiam', 'bomber', 'call', 'prank', 'PHISHER', 'hack','sms bomber','sms bomber', 'SIAMRAHMAN'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'siamttview = siamttview.siamttview:send',
                
            ],
    },
    python_requires='>=3.6'
)
