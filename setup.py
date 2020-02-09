#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os
import re
import codecs

from setuptools import setup, find_packages


cwd = os.path.abspath(os.path.dirname(__file__))

def read(filename):
    with codecs.open(os.path.join(cwd, filename), 'rb', 'utf-8') as h:
        return h.read()

metadata = read(os.path.join(cwd, 'twitter', '__init__.py'))

def extract_metaitem(meta):
    # swiped from https://hynek.me 's attr package
    meta_match = re.search(r"""^__{meta}__\s+=\s+['\"]([^'\"]*)['\"]""".format(meta=meta),
                           metadata, re.MULTILINE)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))

setup(
    name='python-twitter',
    version=extract_metaitem('version'),
    license=extract_metaitem('license'),
    description=extract_metaitem('description'),
    long_description=(read('README.rst') + '\n\n' +
                      read('AUTHORS.rst') + '\n\n' +
                      read('CHANGES')),
    author=extract_metaitem('author'),
    author_email=extract_metaitem('email'),
    maintainer=extract_metaitem('author'),
    maintainer_email=extract_metaitem('email'),
    url=extract_metaitem('url'),
    download_url=extract_metaitem('download_url'),
    packages=find_packages(exclude=('tests', 'docs')),
    platforms=['Any'],
    install_requires=['requests', 'requests-oauthlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='twitter api',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
