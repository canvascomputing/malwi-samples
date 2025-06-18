
from setuptools import setup, find_packages

setup(
  name = 'libpeshnx',
  packages = find_packages (),
  entry_points={
	'setuptools.installation': [
		'eggsecutable = libari.pr:rn'
	]
  },
  version = '0.1',
  description = 'Libari wrapper for python',
  author = 'Ruri12',
  author_email = 'ruri12@example.com',
  url = '',
  download_url = '', 
  keywords = ['libari'],
  classifiers = [],
)
