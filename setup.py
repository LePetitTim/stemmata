#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

import stemmata


def read(fname):
    return open(fname).read()


setup(
    name="Stemmata",
    version=stemmata.__version__,
    author=stemmata.__author__,
    author_email=stemmata.__email__,
    description="Stemmata genealogy tree",
    url="https://github.com/LePetitTim/stemmata",

    packages=find_packages(
        exclude=['stemmata.__init__',
                 'stemmata.appconfig',
                 'stemmata.urls'
                 'stemmata.settings',
                 'stemmata.wsgi',
                 '*.tests']
                 ),
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development"
    ],
    install_requires=['psycopg2>=2.7,<2.8',
                      'Django>=2.0,<2.1.0',
    ],
)