aliuacademy.org - Development
*****************************

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

To run the tests, initialise the database and run the development server::

  ./init_dev.sh

To run the development server without initialising the database::

  python manage.py runserver

Browse to http://localhost:8085/

Click *Login* and login as a standard web user or a member of staff::

  Username      web
  Password      letmein

  Username      staff
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
