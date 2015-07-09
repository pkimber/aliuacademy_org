# -*- encoding: utf-8 -*-


# PJK 20/03/2015
# This document shows a person using the 'local_settings.py' file :)
# https://github.com/learningequality/ka-lite/wiki/Raspberry-Pi:-Performance-tuning

# PJK 11/03/2015 Can't find these in the documentation, but we seem to need
# them.  Perhaps they are to do with Django 1.7?
PRODUCTION_PORT = 8008
KALITE_TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# PJK 20/03/2015
CHERRYPY_THREAD_COUNT = 20

# PJK 20/03/2015
# WSGI_APPLICATION = 'project.wsgi.application'

# PJK 20/03/2015 - For the actual 'aliuacademy_org' Django application
TESTING = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "logfile",
            'maxBytes': 500000,
            'backupCount': 10,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}
