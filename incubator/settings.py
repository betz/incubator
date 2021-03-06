"""
Django settings for incubator project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cw2lz4ml1#r%=h2aax8_)=q$v(+&9&)n5xxk5g!9og%ityd!@#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'debug_toolbar',
    'bootstrap3',
    'datetimewidget',
    'activelink',
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'analytical',

    'incubator',
    'events',
    'users',
    'projects',
    'space',
    'stock',
    'django_nyt',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
    'django_extensions',
    'realtime',
    'actstream',
    'manmail',
    'redir',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'incubator.urls'

WSGI_APPLICATION = 'incubator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-be'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "/"

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
    "space.context_processors.state",
    "sekizai.context_processors.sekizai",
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'incubator.hashers.MediaWikiHasher',
)


MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('incubator.drf.ReadOnlyPermission',),
    'DEFAULT_PAGINATION_CLASS': 'incubator.drf.AnachistPageNumberPagination',
    'UNICODE_JSON': False,
}

# no tailing slash
ROOT_URL = "https://urlab.be"


BANK_ACCOUNT = "BE66 0017 6764 5043"

REDIS_HOST = "rainbowdash.lan"
REDIS_PORT = 6379
FAKE_REDIS = True

USE_WAMP = False
CROSSBAR_URL = 'http://localhost:8080/publish'
CROSSBAR_SECRET = "Vairy secrette"
CROSSBAR_REALM = 'realm'

INFLUX_HOST = "localhost"
INFLUX_PORT = 8086
INFLUX_USER = "derp"
INFLUX_PASS = "derp"

LOGIN_URL = '/auth/login/'

WIKI_ATTACHMENTS_EXTENSIONS = (
    'jpg',
    'jpeg',
    'png',
    'tex',
    'py',
    'ppt',
    'pptx',
    'pdf',
    'zip',
    'tar',
    'gz',
)

ACTSTREAM_SETTINGS = {
    'USE_JSONFIELD': True
}

PIWIK_DOMAIN_PATH = 'piwik.urlab.be'
PIWIK_SITE_ID = '2'

MINIMAL_MAIL_APPROVERS = 3

try:
    from incubator.local_settings import *
except ImportError:
    pass
