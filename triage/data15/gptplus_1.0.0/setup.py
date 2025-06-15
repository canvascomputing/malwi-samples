from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gptplus',
    version='1.0.0',
    author='Xeroline',
    author_email='ejxbhpx@hldrive.com',
    description="GPT-4 Turbo is a cutting-edge language model developed by OpenAI, now available for free access through web engineering advancements.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.google.com',
    project_urls={
        'Bug Tracker': 'https://www.google.com/search?q=never+gonna+give+you+up',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['requests'],
    python_requires='>=3.6'
)