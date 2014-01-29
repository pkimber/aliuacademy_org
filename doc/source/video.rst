Video
*****

.. highlight:: bash

Videos are uploaded to the following folder::

  /home/web/repo/ftp/aliuacademy_org/site/static/academy/

To create this folder on a new system::

  sudo -i -u aliuacademy_org
  mkdir /home/web/repo/ftp/aliuacademy_org/site/static/academy/

After uploading videos, check permissions as follows::

  chmod -R 755 /home/aliuacademy_org/site
  chown -R aliuacademy_org:aliuacademy_org /home/aliuacademy_org/site
