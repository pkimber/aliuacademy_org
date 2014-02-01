Video
*****

.. highlight:: bash

To copy videos to the folders, start the file manager with root permission::

  sudo -i
  nautilus /home/web/repo/ftp/aliuacademy_org/site/static/

Copy the videos to a sub-folder within the ``academy`` folder::

  /home/web/repo/ftp/aliuacademy_org/site/static/academy/

After copying the videos to the folders::

  exit

After uploading videos, update permissions as follows::

  sudo -i
  find /home/aliuacademy_org/site -type f -exec chmod 0664 {} \;
  find /home/aliuacademy_org/site -type d -exec chmod 2775 {} \;
  find /home/aliuacademy_org/site -exec chown aliuacademy_org:web {} \;
  exit

To add the videos to the web site::

  sudo -i -u web
  aliuacademy_org.sh init_app_aliu
  exit
