#!/usr/bin/env python

# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from os.path import abspath, dirname, join


from setuptools import setup, find_packages

BASE_DIR = dirname(abspath(__file__))
VERSION_FILE = join(BASE_DIR, 'stix', 'version.py')


def get_version():
    with open(VERSION_FILE) as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")


def get_long_description():
    with open('README.rst') as f:
        return f.read()


install_requires = [
    'lxml>=2.2.3 ; python_version == "2.7" or python_version >= "3.5"',
    'lxml>=2.2.3,<4.4.0 ; python_version > "2.7" and python_version < "3.5"',
    'python-dateutil',
    'cybox>=2.1.0.13,<2.1.1.0',
    'mixbox>=1.0.2',
]


setup(
    name="stix",
    version=get_version(),
    author="STIX Project, MITRE Corporation",
    author_email="stix@mitre.org",
    description="An API for parsing and generating STIX content.",
    long_description=get_long_description(),
    url="http://stix.mitre.org",
    packages=find_packages(),
    install_requires=install_requires,
    license="BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
