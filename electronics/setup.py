# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in electronics/__init__.py
from electronics import __version__ as version

setup(
	name='electronics',
	version=version,
	description='Electronics',
	author='Shahid',
	author_email='shahid@codessoft.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
