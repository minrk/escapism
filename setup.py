#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Min RK.
# Distributed under the terms of the MIT License.

from __future__ import print_function
import os
import sys

from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'escapism.py')) as f:
    exec(f.read(), {}, version_ns)


class bdist_egg_disabled(bdist_egg):
    """Disabled version of bdist_egg

    Prevents setup.py install from performing setuptools' default easy_install,
    which it should never ever do.
    """
    def run(self):
        sys.exit("Aborting implicit building of eggs. Use `pip install .` to install from source.")


setup_args = dict(
    name                = 'escapism',
    version             = version_ns['__version__'],
    py_modules          = ['escapism'],
    description         = "Simple, generic API for escaping strings.",
    long_description    = """There is no reason to install this package on its own.""",
    author              = "Min RK",
    author_email        = "benjaminrk@gmail.com",
    url                 = "https://github.com/minrk/escapism",
    license             = "MIT",
    classifiers         = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass = {
        'bdist_egg': bdist_egg if 'bdist_egg' in sys.argv else bdist_egg_disabled,
    }
)

if __name__ == '__main__':
    setup(**setup_args)
