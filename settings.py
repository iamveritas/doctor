"""
Django settings for lykar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(__file__)

FEEDBACK_EMAIL_RECEIVERS = (
    'geo.savchuk@gmail.com',
    'hyralmisha@gmail.com',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fyr4^5ciw&#chl)cxm3@(qzp%-7yru)#1vfp3_dcw(rpa^of_yt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.home',
    'apps.rules',
    'apps.advertisement',
    'apps.faq',
    'apps.contacts',
    'apps.adminpanel',
    'apps.internal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static-collect/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

try:
    from local_settings import *
except ImportError:
    pass