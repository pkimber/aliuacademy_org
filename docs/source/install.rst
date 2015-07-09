Install
*******

Check
=====

1. The Windows user name must **not** contain spaces.

   You can check the user name by clicking on the *Start* button and finding
   the name about the *Document* menu item.

2. The computer must not have python 2 installed.

   Go to *Control Panel*, *Uninstall a program* and make sure python is not in
   the list of installed programs.  If it is, then *Uninstall* it.

Install
=======

Run the ``AliuAcademy-1.0.0.0.exe`` installer.

.. note:: The version number might be different than the one shown above e.g.
          ``AliuAcademy-1.0.1.6.exe``.

At the *Install Python?* prompt, click *Yes*

At the *Server Information* page leave the *Server name* and *Server
description* empty.

At the *Admin Information* page enter a *Username* and *Password*.

.. note:: Make a careful note of the *Username* and *Password*.  You will need
          them to login into the site.

At the *Server Configuration* page, choose the option to *Do not run the server
at startup*.

At the *Select Additional Tasks* page, do **not** tick the *Create a desktop
icon* box.

Run
***

If you don't have the *AliuAcademy* icon in the task bar:

  Click on the *Start* button, select *All Programs*, *AliuAcademy*, and click
  on *AliuAcademy*.

Right click on the *AliuAcademy* icon in the task bar and click *Start Server*.

If you get Firewall warnings, allow *AliuAcademy* through.

Right click on the *AliuAcademy* icon in the task bar and click *Load in
browser*.

Videos and Course Material
==========================

Start by locating the ``content`` folder on your computer.  This will probably
be in the following folder::

  C:\Program Files\AliuAcademy\aliuacademy_org\content\

If not, try this folder::

  C:\Program Files (x86)\AliuAcademy\aliuacademy_org\content\

Within the ``content`` folder create folders for the university, course and
topic e.g. for ``Exeter`` university, the ``IT`` course and the ``Intro``
topic::

  C:\Program Files\AliuAcademy\aliuacademy_org\content\Exeter\IT\Intro\

Copy videos into the topic folder e.g. ``Intro``.

Create a ``ware`` sub-folder for the course documents::

  C:\Program Files\AliuAcademy\aliuacademy_org\content\Exeter\IT\Intro\ware\

Copy course materials into the ``ware`` folder.

Run the *AliuAcademy* site (see *Run* section above).

Click *Login* in the top right hand corner of the site and enter your login
details.

Click *Settings* and then *Rebuild DB*.

Your universities, courses, topics, videos and course materials should now
appear on the site.
