#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Min RK.
# Distributed under the terms of the MIT License.

from __future__ import print_function
import os
import sys
from glob import glob

from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'escapism.py')) as f:
    exec(f.read(), {}, version_ns)


setup_args = dict(
    name                = 'escapism',
    version             = version_ns['__version__'],
    py_modules          = ['escapism'],
    description         = "Simple, generic API for escaping strings.",
    long_description    = """There is no reason to install this package on its own.""",
    author              = "Min RK",
    author_email        = "benjaminrk@gmail.com",
    url                 = "https://github.com/minrk/escapism",
    license             = "BSD",
    classifiers         = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

if any(bdist in sys.argv for bdist in ('bdist_wheel', 'bdist_egg')):
    import setuptools

if __name__ == '__main__':
    setup(**setup_args)
