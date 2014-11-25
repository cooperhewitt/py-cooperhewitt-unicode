#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.unicode',
    namespace_packages=['cooperhewitt', 'cooperhewitt.unicode'],
    version='0.11',
    description='Tools for working with Unicode data',
    author='Smithsonian Cooper-Hewitt National Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-unicode',
    requires=[],
    packages=packages,
    scripts=[
        'scripts/ucd-name',
        'scripts/ucd-build-lookup'
        ],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-unicode/releases/tag/v0.11',
    license='BSD')
