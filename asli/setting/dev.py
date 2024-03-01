from asli.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&p=2wfyz^9(m$i#v&d_l_aoa-r&4ew1+)^bv*ea2j958ffew8n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#INSTALLED_APPS = []


# sites framework
SITE_ID = 3


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media/'


STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

# debug_toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]


#compressor settings
COMPRESS_ENABLED = True

