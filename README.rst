aliuacademy.org
***************

Development
===========

Install
-------

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``settings`` folder to make sure a file
has been created for you)::

  mkvirtualenv dev_aliuacademy_org
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=settings.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
  echo "export SECRET_KEY=\"the_secret_key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../../app/cms
  add2virtualenv ../../app/base
  add2virtualenv ../../app/login
  add2virtualenv .
  deactivate

To check the order of the imports::

  workon dev_aliuacademy_org
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g::

  /home/patrick/repo/dev/project/aliuacademy_org
  /home/patrick/repo/dev/app/login
  /home/patrick/repo/dev/app/base
  /home/patrick/repo/dev/app/cms

Testing
-------

We use ``pytest-django``::

  workon dev_aliuacademy_org
  find . -name '*.pyc' -delete
  py.test

To stop on first failure::

  py.test -x

Usage
-----

::

  workon dev_aliuacademy_org

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_aliu && \
      django-admin.py runserver

Release and Deploy
==================

https://github.com/pkimber/docs::

  chmod -R 755 /home/aliuacademy_org/site
  chown -R aliuacademy_org:aliuacademy_org /home/aliuacademy_org/site
