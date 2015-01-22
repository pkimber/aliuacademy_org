aliuacademy.org
***************

Development
===========

Install
-------

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-aliuacademy_org
  source venv-aliuacademy_org/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

To set-up a demo database for development::

  ./init_test.sh

Release and Deploy
==================

https://www.pkimber.net/open/
