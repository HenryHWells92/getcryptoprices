# setup file for agalea91's cryptocompare api connectors

from setuptools import setup, find_packages

setup(
    name="getcryptoprices",
    version="0.0.1",
    install_requires=["pandas", "requests", "datetime", "matplotlib", "uuid"],
	packages = find_packages(exclude=['contrib', 'docs', 'tests'])
)