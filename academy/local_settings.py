# -*- encoding: utf-8 -*-


# PJK 20/03/2015
# This document shows a person using the 'local_settings.py' file :)
# https://github.com/learningequality/ka-lite/wiki/Raspberry-Pi:-Performance-tuning

# PJK 11/03/2015 Can't find these in the documentation, but we seem to need
# them.  Perhaps they are to do with Django 1.7?
PRODUCTION_PORT = 8085
KALITE_TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# PJK 20/03/2015
CHERRYPY_THREAD_COUNT = 20

# PJK 20/03/2015
# WSGI_APPLICATION = 'project.wsgi.application'

# PJK 20/03/2015 - For the actual 'aliuacademy_org' Django application
TESTING = False
