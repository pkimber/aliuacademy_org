Video
*****

.. highlight:: bash

Videos are uploaded to the following folder::

  /home/web/repo/ftp/aliuacademy_org/site/static/academy/

To create this folder on a new system::

  sudo -i -u aliuacademy_org
  mkdir /home/web/repo/ftp/aliuacademy_org/site/static/academy/

After uploading videos, update permissions as follows::

  find /home/aliuacademy_org/site -type f -exec chmod 0664 {} \;
  find /home/aliuacademy_org/site -type d -exec chmod 0775 {} \;
