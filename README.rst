AliauAcademy Installer for Windows
==================================

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
