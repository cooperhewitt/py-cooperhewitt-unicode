#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.unicode',
    namespace_packages=['cooperhewitt', 'cooperhewitt.unicode'],
    version='0.1',
    description='Tools for working with Unicode',
    author='Smithsonian Cooper-Hewitt National Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-unicode',
    requires=[],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-unicode/releases/tag/v0.1',
    license='BSD')
