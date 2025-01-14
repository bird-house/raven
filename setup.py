#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages

version = __import__('raven').__version__
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

reqs = [line.strip() for line in open('requirements.txt')]
docs_reqs = [
    'sphinx>=1.7',
    'sphinx-autoapi',
    'nbsphinx',
    'sphinx-autodoc-pywps @ git+ssh://git@github.com/huard/sphinx-autodoc-pywps.git#egg=sphinx_autodoc_pywps'
]

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'License :: OSI Approved :: MIT License',
]

setup(name='raven',
      version=version,
      description="A Web Processing Service for Climate Data Analysis.",
      long_description=README + '\n\n' + CHANGES,
      author="David Huard",
      author_email='huard.david@ouranos.ca',
      url='https://github.com/huard/raven',
      classifiers=classifiers,
      license="MIT license",
      keywords='wps pywps birdhouse raven hydrology gis',
      packages=find_packages(),
      include_package_data=True,
      install_requires=reqs,
      extras_require={'docs': docs_reqs},
      entry_points={
          'console_scripts': [
              'raven=raven.cli:cli',
          ]}, )
