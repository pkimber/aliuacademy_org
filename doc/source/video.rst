Video
*****

.. highlight:: bash

Videos are uploaded to the following folder::

  /home/web/repo/ftp/aliuacademy_org/site/static/academy/

To upload videos, start the file manager with root permission::

  sudo -i
  nautilus /home/web/repo/ftp/aliuacademy_org/site/static/

After uploading videos, update permissions as follows::

  sudo -i
  find /home/aliuacademy_org/site -type f -exec chmod 0664 {} \;
  find /home/aliuacademy_org/site -type d -exec chmod 2775 {} \;
  find /home/aliuacademy_org/site -type f -exec chown aliuacademy_org:web {} \;
  find /home/aliuacademy_org/site -type d -exec chown aliuacademy_org:web {} \;
