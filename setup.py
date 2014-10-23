from __future__ import unicode_literals
from setuptools import setup, find_packages
import os

import dj_tornado

here = os.path.dirname(__file__) 

version = ".".join(map(str, dj_tornado.__version__))
author_first, author_last, author_email = dj_tornado.__author__.split()
author = " ".join((author_first, author_last))
author_email = author_email.strip('<>')
description = dj_tornado.__doc__
README = open(os.path.join(here, 'README.md')).read()
install_requires = ['tornado', 'dj-static']

setup(name='django-tornado',
      version=version,
      description=description,
      long_description=README,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Information Technology',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Framework :: Django'
      ],
      keywords='django in tornado as management command',
      author=author,
      author_email=author_email,
      url='http://github.com/weargoggles/django-tornado',
      license='MIT License',
      packages=find_packages(),
      include_package_data=True,
      test_suite='dj_tornado.test.load_suite',
      zip_safe=False,
      install_requires=install_requires,
)
