AliuAcademy - Installer, Script Files and Django Project
********************************************************

Folders
=======

The folder structure for this project is confusing::

  # installer (uses inno setup compiler)
  /

  # batch and script files to start/stop the server
  aliuacademy_org/

  # django project
  aliuacademy_org/academy/

The Django project is in the ``aliuacademy_org/academy/`` folder.  To carry out
development on this project::

  cd aliuacademy_org/academy/
  # follow the instructions in the 'README-DEV.rst' file.

Content
-------

::

  C:\Program Files (x86)\AliuAcademy\aliuacademy_org\content\

For testing, you could use a structure of universities and courses like this::

  Exeter
    IT
      Intro

Installer for Windows
=====================

This project provides a smoother way to install and run AliauAcademy in a
Windows Machine.

This project was built using the following software:

- Inno Setup 5.5.3 [Download] (http://files.jrsoftware.org/is/5/)
- Microsoft Visual Studio Express 2012 [Download]
  (https://www.microsoft.com/en-us/download/details.aspx?id=34673)

  Download ``wdexpress_full.exe`` and run it.  This will download and install
  Visual Studio.  The other download is an ``iso`` file.

- Git

  https://git-scm.com/download/win

.. note:: install with the option to place the ``git`` executable in the path,
          so it can be run within ``cmd``.

Instructions to update Microsoft Visual Studio 2012:

Steps to update:

- Click on TOOLS menu
- Select Extensions and Updates... then another dialog will appear.
- Click on Update.

Install the downloaded update in your machine:

- Click on BUILD.
- Select Build Solution.

Instructions to build ``AliuAcademy.exe``:

- Clone this repository;
- Open `cmd` -- the Windows command prompt;
- Run `make.vbs` and wait until the file is built;
- The output file named ``KALiteSetup.exe`` will appear within this project
  folder.

If you wish to build it using Wine, run the following line::

  wine inno-compiler/ISCC.exe installer-source/KaliteSetupScript.iss
