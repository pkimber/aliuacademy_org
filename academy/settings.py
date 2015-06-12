import logging
import os
import platform
# PJK 11/03/2015 I don't think we need 'fle_utils'
#from fle_utils.settingshelper import import_installed_app_settings

# PJK 11/03/2015
from django.core.urlresolvers import reverse_lazy
from django.utils import six


# PJK 11/03/2015 Copied from 'kalite/distributed/settings.py'
########################
# Functions, for support
########################

def USER_FACING_PORT():
    global PROXY_PORT
    global PRODUCTION_PORT
    return PROXY_PORT or PRODUCTION_PORT


##############################
# Functions for querying settings
##############################

def package_selected(package_name):
    global CONFIG_PACKAGE
    return bool(CONFIG_PACKAGE) and bool(package_name) and package_name.lower() in CONFIG_PACKAGE


##############################
# Basic setup
##############################
try:
    from local_settings import *
    import local_settings
except ImportError:
    local_settings = object()


# Used everywhere, so ... set it up top.
DEBUG          = getattr(local_settings, "DEBUG", False)

CENTRAL_SERVER = False  # Hopefully will be removed soon.

##############################
# Basic setup of logging
##############################

# Set logging level based on the value of DEBUG (evaluates to 0 if False, 1 if True)
LOGGING_LEVEL = getattr(local_settings, "LOGGING_LEVEL", logging.DEBUG if DEBUG else logging.INFO)
LOG = getattr(local_settings, "LOG", logging.getLogger("academy"))
TEMPLATE_DEBUG = getattr(local_settings, "TEMPLATE_DEBUG", DEBUG)

logging.basicConfig()
LOG.setLevel(LOGGING_LEVEL)
logging.getLogger("requests").setLevel(logging.WARNING)  # shut up requests!


##############################
# Basic Django settings
##############################

# Not really a Django setting, but we treat it like one--it's eeeeverywhere.
PROJECT_PATH = os.path.realpath(getattr(local_settings, "PROJECT_PATH", os.path.dirname(os.path.realpath(__file__)))) + "/"

BUILD_INDICATOR_FILE = os.path.join(PROJECT_PATH, "_built.touch")
BUILT = os.path.exists(BUILD_INDICATOR_FILE)  # whether this installation was processed by the build server

LOCALE_PATHS   = getattr(local_settings, "LOCALE_PATHS", (PROJECT_PATH + "/../locale",))
LOCALE_PATHS   = tuple([os.path.realpath(lp) + "/" for lp in LOCALE_PATHS])

DATABASES      = getattr(local_settings, "DATABASES", {
    "default": {
        "ENGINE": getattr(local_settings, "DATABASE_TYPE", "django.db.backends.sqlite3"),
        "NAME"  : getattr(local_settings, "DATABASE_PATH", os.path.join(PROJECT_PATH, "database", "data.sqlite")),
        "OPTIONS": {
            "timeout": 60,
        },
    }
})

INTERNAL_IPS   = getattr(local_settings, "INTERNAL_IPS", ("127.0.0.1",))
ALLOWED_HOSTS = getattr(local_settings, "ALLOWED_HOSTS", ['*'])


# PJK 11/03/2015 Copied from 'kalite/distributed/settings.py'
########################
# Ports & Accessibility
########################

PRODUCTION_PORT = getattr(local_settings, "PRODUCTION_PORT", 8008)

#proxy port is used by nginx and is used by Raspberry Pi optimizations
PROXY_PORT = getattr(local_settings, "PROXY_PORT", None)


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE      = getattr(local_settings, "TIME_ZONE", None)
#USE_TZ         = True  # needed for timezone-aware datetimes (particularly in updates code)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE  = getattr(local_settings, "LANGUAGE_CODE", "en")

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
# PJK 22/03/2015
USE_I18N       = False #getattr(local_settings, "USE_I18N", True)

# If you set this to True, Django will format dates, numbers and
# calendars according to the current locale
# PJK 22/03/2015
USE_L10N       = False #getattr(local_settings, "USE_L10N", False)

MEDIA_URL      = getattr(local_settings, "MEDIA_URL", "/media/")
MEDIA_ROOT     = os.path.normpath(os.path.join(PROJECT_PATH, '..', 'content'))

STATIC_URL     = getattr(local_settings, "STATIC_URL", "/static/")
STATIC_ROOT    = os.path.realpath(getattr(local_settings, "STATIC_ROOT", PROJECT_PATH + "/static/")) + "/"

 # Make this unique, and don't share it with anybody.
SECRET_KEY     = getattr(local_settings, "SECRET_KEY", "8qq-!fa$92i=s1gjjitd&%s@4%ka9lj+=@n7a&fzjpwu%3kd#u")

LANGUAGE_COOKIE_NAME    = "django_language"

# PJK 11/03/2015
# ROOT_URLCONF = "kalite.distributed.urls"
ROOT_URLCONF = 'project.urls'

# PJK 11/03/2015
# INSTALLED_APPS = (
#     "django.contrib.admin",  # this and the following are needed to enable django admin.
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.messages",
#     "django.contrib.sessions",
#     "django_extensions", # needed for clean_pyc (testing)
#     "kalite.distributed",
# )


DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'reversion',
)

LOCAL_APPS = (
    'project',
    'base',
    'login',
    'web',
)

# PJK 11/03/2015
KA_LITE_APPS = (
    'django_extensions', # needed for clean_pyc (testing)
    'fle_utils.config',  # default_language
    'distributed',
    'django_cherrypy_wsgiserver',
)


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + KA_LITE_APPS


# PJK 11/03/2015
# if not BUILT:
print()
print()
print()
#     INSTALLED_APPS += (
#         "fle_utils.testing",
#         "academy.testing",
#     ) + getattr(local_settings, 'INSTALLED_APPS', tuple())

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # PJK 31/03/2015
    # "django.contrib.messages.middleware.MessageMiddleware",  # needed for django admin
    # PJK 20/03/2015
    # "django_snippets.session_timeout_middleware.SessionIdleTimeout",
) + getattr(local_settings, 'MIDDLEWARE_CLASSES', tuple())

TEMPLATE_DIRS  = tuple()  # will be filled recursively via INSTALLED_APPS
# PJK 19/03/2015
# STATICFILES_DIRS = (os.path.join(PROJECT_PATH, '..', 'static-libraries'),)  # libraries common to all apps

DEFAULT_ENCODING = 'utf-8'

########################
# Storage and caching
########################

# Sessions use the default cache, and we want a local memory cache for that.
CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Separate session caching from file caching.
SESSION_ENGINE = getattr(local_settings, "SESSION_ENGINE", 'django.contrib.sessions.backends.cache' + (''))

# Use our custom message storage to avoid adding duplicate messages
# MESSAGE_STORAGE = 'fle_utils.django_utils.NoDuplicateMessagesSessionStorage'

# disable migration framework on tests
# PJK 11/03/2015
# SOUTH_TESTS_MIGRATE = False

# Default to a 20 minute timeout for a session - set to 0 to disable.
SESSION_IDLE_TIMEOUT = getattr(local_settings, "SESSION_IDLE_TIMEOUT", 1200)

########################
# After all settings, but before config packages,
#   import settings from other apps.
#
# This allows app-specific settings to be localized and augment
#   the settings here, while also allowing
#   config packages to override settings.
########################

# PJK 11/03/2015 I don't think we need 'fle_utils'
# import_installed_app_settings(INSTALLED_APPS, globals())

if 'CACHE_NAME' in locals():
    if CACHE_NAME == "file_based_cache":
        LOG.debug("Cache location = %s" % CACHE_LOCATION)
    else:
        LOG.debug("Using %s caching" % CACHE_NAME)

# Override
KHAN_EXERCISES_DIRPATH = getattr(local_settings, "KHAN_EXERCISES_DIRPATH", os.path.join(STATIC_ROOT, "khan-exercises"))
CHERRYPY_PORT = getattr(local_settings, "CHERRYPY_PORT", PRODUCTION_PORT)
TEST_RUNNER = KALITE_TEST_RUNNER

LOG.debug("======== MIDDLEWARE ========")
LOG.debug("\n".join(MIDDLEWARE_CLASSES))
LOG.debug("====== INSTALLED_APPS ======")
LOG.debug("\n".join(INSTALLED_APPS))
LOG.debug("============================")

########################
# IMPORTANT: Do not add new settings below this line
#
# Everything that follows is overriding default settings, depending on CONFIG_PACKAGE

# config_package (None|RPi) alters some defaults e.g. different defaults for Raspberry Pi(RPi)
# autodetect if this is a Raspberry Pi-type device, and auto-set the config_package
#  to override the auto-detection, set CONFIG_PACKAGE=None in the local_settings
########################

CONFIG_PACKAGE = getattr(local_settings, "CONFIG_PACKAGE", "RPi" if (platform.uname()[0] == "Linux" and platform.uname()[4] == "armv6l") else [])

# PJK 11/03/2015 - was - if isinstance(CONFIG_PACKAGE, basestring):
if isinstance(CONFIG_PACKAGE, six.string_types):
    CONFIG_PACKAGE = [CONFIG_PACKAGE]
CONFIG_PACKAGE = [cp.lower() for cp in CONFIG_PACKAGE]


# Config for Raspberry Pi distributed server
if package_selected("RPi"):
    LOG.info("RPi package selected.")
    # nginx proxy will normally be on 8008 and production port on 7007
    # If ports are overridden in local_settings, run the optimizerpi script
    PRODUCTION_PORT = getattr(local_settings, "PRODUCTION_PORT", 7007)
    PROXY_PORT = getattr(local_settings, "PROXY_PORT", 8008)
    assert PRODUCTION_PORT != PROXY_PORT, "PRODUCTION_PORT and PROXY_PORT must not be the same"
    CHERRYPY_PORT = PRODUCTION_PORT  # re-do above override AGAIN.
    #SYNCING_THROTTLE_WAIT_TIME = getattr(local_settings, "SYNCING_THROTTLE_WAIT_TIME", 1.0)
    #SYNCING_MAX_RECORDS_PER_REQUEST = getattr(local_settings, "SYNCING_MAX_RECORDS_PER_REQUEST", 10)

    PASSWORD_ITERATIONS_TEACHER = getattr(local_settings, "PASSWORD_ITERATIONS_TEACHER", 2000)
    PASSWORD_ITERATIONS_STUDENT = getattr(local_settings, "PASSWORD_ITERATIONS_STUDENT", 500)

    ENABLE_CLOCK_SET = getattr(local_settings, "ENABLE_CLOCK_SET", True)


if package_selected("UserRestricted"):
    LOG.info("UserRestricted package selected.")

    if CACHE_TIME != 0 and not hasattr(local_settings, KEY_PREFIX):
        KEY_PREFIX += "|restricted"  # this option changes templates
    DISABLE_SELF_ADMIN = True  # hard-code facility app setting.

if package_selected("Demo"):
    LOG.info("Demo package selected.")

    CENTRAL_SERVER_HOST = getattr(local_settings, "CENTRAL_SERVER_HOST", "staging.learningequality.org")
    SECURESYNC_PROTOCOL = getattr(local_settings, "SECURESYNC_PROTOCOL", "http")
    DEMO_ADMIN_USERNAME = getattr(local_settings, "DEMO_ADMIN_USERNAME", "admin")
    DEMO_ADMIN_PASSWORD = getattr(local_settings, "DEMO_ADMIN_PASSWORD", "pass")

    MIDDLEWARE_CLASSES += ('distributed.demo_middleware.StopAdminAccess','distributed.demo_middleware.LinkUserManual','distributed.demo_middleware.ShowAdminLogin',)

# PJK 11/03/2015 TODO Check if we want to use sendfile (or not)
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'

# PJK 11/03/2015
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('web.university.list')
