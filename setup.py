from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-datapub',
	version=version,
	description="Publishing datasets as nanopublications.",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Jim McCusker',
	author_email='mccusker@gmail.com',
	url='https://github.com/jimmccusker/ckanext-datapub/wiki',
	license='Apache 2.0 License',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datapub'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.datapub:PluginClass
        datapub=ckanext.datapub.plugin:DatapubPlugin
	""",
)
