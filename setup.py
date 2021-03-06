##############################################################################
#
# Copyright (c) 2008-2010 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

__version__ = '0.4dev'

import os
import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]
PY3 = py_version[0] == 3

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    README = ''
    CHANGES = ''

install_requires = [
    'pyramid>=1.1',
]

tests_require = install_requires + [
    'WebTest',
]

if not PY3:
    tests_require.extend([
        'pyamf',
    ])

testing_extras = tests_require + [
    'nose',
    'coverage',
]

docs_require = [
    'Sphinx',
    'docutils',
]

setup(name='pyramid_rpc',
      version=__version__,
      description='RPC support for the Pyramid web framework',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pyramid",
        ],
      keywords='web wsgi pyramid pylons xml-rpc',
      author="Ben Bangert",
      author_email="ben@groovie.org",
      url="https://github.com/Pylons/pyramid_rpc",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require = {
          'testing':testing_extras,
          'docs':docs_require,
          'amf':['pyamf'],
          },
      test_suite="pyramid_rpc.tests",
      )
