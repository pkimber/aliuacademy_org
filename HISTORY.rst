KB Software
***********

.. highlight:: bash

.. important:: Don't forget to ``unset DJANGO_SETTINGS_MODULE``

::

  cd /home/patrick/repo/dev/project/lite_aliuacademy_org
  deactivate
  unset DJANGO_SETTINGS_MODULE
  ./setup_unix.sh

WIP
===

Earlier
-------

::

  git clone https://github.com/learningequality/ka-lite.git

Discussed with Tim.  The KA-Lite installer installs python 2.7 and I guess it
adds it to the PATH.  I will do this manually.

I have installed C:\Python27 and C:\Python34

For testing the KA-Lite project, I use python 2.7::

  SET PATH=%PATH%;C:\python27
  cd C:\Users\patrick\repo\dev\ka-lite\
  SET PATH=%PATH%;C:\python27
  # runs in the background
  scripts\serverstart.bat

This is running migrations, collect static etc using these management
commands::

  ka-lite\kalite\distributed\management\commands\kaserve.py
  ka-lite\kalite\distributed\management\commands\setup.py

Instructions after::

  CONGRATULATIONS! You've finished updating the KA Lite server software.
  Please run 'C:\Users\patrick\repo\dev\ka-lite\start.bat' to start the server.

To run (takes a few seconds to get started)::

  start.bat

Browse to http://127.0.0.1:8008/

04/03/2015
----------

``Downloads`` in this folder for the ``python-packages``.  Upgraded::

  Django 1.7.5

https://learningequality.org/ka-lite/user-guides/latest::

  ./setup_unix.sh
  # do not run automatically in the background

  # to run after it has been set-up
  ./start.sh

11/03/2015
----------

::

  NameError: name 'execfile' is not defined
  Called from 'python-packages/fle_utils'

Not sure if we need ``fle_utils``::

  git mv python-packages/fle_utils python-packages/do-not-need-fle_utils

Had to create ``kalite/local_settings.py``.  Perhaps I should move settings
from ``local_settings.py`` to ``kalite/settings.py``.  Need to check if they
are required for Windows as well as linux.

Making my own ``python-packages/fle_utils`` and copying a few of the functions
over.

14/03/2015
----------

Trying to get this script working::

  kalite/distributed/management/commands/setup.py

To try and ``makemigrations``::

  $ cd kalite
  $ python manage.py makemigrations fle_utils.config
  App 'fle_utils.config' could not be found. Is it in INSTALLED_APPS?

19/03/2015
----------

Windows::

  setup_windows.bat

I have python 2 and python 3 installed::

  CommandError:
  You must have Python version 3.4.x installed.
  Your version is: 2.7.8

Removing python 2.  I then had to re-install python 3 to get the "Python3.exe"
key in the registry at::

  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"

The registry is searched in::

  scripts\python.bat

git push::

  git push origin HEAD:203-kalite-installer

To run management commands (on linux)::

  python3 academy/manage.py shell

20/03/2015
----------

Struggling because I couldn't see what CherryPy was doing.  To solve the
problem:

  # scripts/serverstart.sh
  # set daemonize=false
  "$pyexec" "$KALITE_DIR/manage.py" kaserve host=0.0.0.0 daemonize=false production=true pidfile="$KALITE_DIR/runcherrypyserver.pid"

  # python-packages/cherrypy/__init__.py
  log.error_file = 'logger.log'

30/05/2015
----------

- Set-up program has a version number now :)
- Renamed test data so Windows is happy.

Issues

- Does not detect existing install of python so we have to "repair".
- Name should be "Aliu" not "Aliua"
- Name of installer should be "aliuacademy-installer-windows" not "aliauacademy-installer-windows"
- exe file name has two dots: "AliuAcademy-1.0.0..exe" should be just one.
- Missing icon on start menu.
- No favicon in the browser tab.
- No option to "Stop Server" after starting.
- "Stop Server" batch file does not stop a running server.