aliuacademy.org
***************

Development
===========

.. note:: All development takes place in the ``aliuacademy_org/academy``
          folder.

Install
-------

Virtual Environment
-------------------

Change into the ``academy`` folder::

  cd academy/

::

  touch .private
  pyvenv-3.4 --without-pip venv-aliuacademy_org
  source venv-aliuacademy_org/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  deactivate
  source venv-aliuacademy_org/bin/activate
  pip install -r requirements/local.txt

Testing
-------

::

  py.test -x

Usage
-----

Change into the ``academy`` folder::

  cd academy/

To set-up a demo database for development::

  ./init_dev.sh

Browse to http://localhost:8000/

Click *Login*::

  Username      web
  Password      letmein

.. note:: The videos in the ``web/tests/data/ftp_static_dir`` folders are not
          actual videos.  I think if you replace them with *proper* videos they
          will play (although this didn't work for me just now)!

Documentation
=============

The documentation can be found in the ``docs`` folder.  To build the
documentation::

  cd academy/
  cd docs && make clean html; cd -
  # to view the docs in your browser
  firefox docs/build/html/index.html &

Release and Deploy
==================

This project is installed onto a Windows computer using a copy of the KALite
installer.
