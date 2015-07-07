AliauAcademy Installer for Windows
**********************************

This project provides a smoother way to install and run AliauAcademy in a
Windows Machine.

Folders
=======

The folder structure for this project is confusing::

  # installer (uses inno setup compiler)
    # batch and script files to start/stop the server
      # django project

Content
-------

::

  C:\Program Files (x86)\AliuaAcademy\aliuacademy_org\content\

For testing, you could use a structure of universities and courses like this::

  Exeter
    IT
      Intro

Installer
=========

This project was built using the following software:

- Inno Setup 5.5.3 [Download] (http://files.jrsoftware.org/is/5/)
- Microsoft Visual Studio Express 2012 [Download]
  (https://www.microsoft.com/en-us/download/details.aspx?id=34673)

  Download ``wdexpress_full.exe`` and run it.  This will download and install
  Visual Studio.  The other download is an ``iso`` file.

- Git

  https://git-scm.com/download/win

  (note: install with the option to place the `git` executable in the path,
  so it can be run within `cmd`)

Instructions to update Microsoft Visual Studio 2012:

Steps to update:

- Click on TOOLS menu
- Select Extensions and Updates... then another dialog will appear.
- Click on Update.

Install the downloaded update in your machine:

- Click on BUILD.
- Select Build Solution.

Instructions to build "AliauAcademy.exe":

- Clone this repository;
- Open `cmd` -- the Windows command prompt;
- Run `git submodule update --init`
- Run `make.vbs` and wait until the file is built;
- The output file named ``KALiteSetup.exe`` will appear within this project
  folder.

To clone this repository, run the following line::

  git clone --recursive https://github.com/timitee/aliauacademy-installer-windows/

(the `--recursive` is required due to the `ka-lite` submodule)

AliuaAcademy

  AliuaAcademy_org folder should be placed directly inside
  ``ka-lite-installer-windows``

If you wish to build it using Wine, run the following line::

  wine inno-compiler/ISCC.exe installer-source/KaliteSetupScript.iss

Installer
=========

The KALite installer runs through as expected:

  Setup will now configure the database...  Please be patient.

  Setup has finished...  Launch KA Lite

  When I click start server, there is a tooltip which pops up above the task
  bar icon to say The server is starting, please wait.  It then says KA Lite is
  running and gives the URL or you can select "Load in browser".
