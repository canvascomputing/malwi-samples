import setup.install_command
kwargs = {
    'name': 'randrange',
    'version': '0.0.2',
    'description': 'Rand range implementation',
    'url': 'https://github.com/randrange/randrange',
    'author': '0xn3va',
    'keywords': ['python', 'range'],
    'long_description': '',
    'long_description_content_type': 'text/markdown',
    'license': 'Apache-2.0',
    'extras_require': {
        'dev': [
            'wheel',
            'twine'
        ]
    },
    'cmdclass': { 'install': setup.install_command.InstallCommand }
}
