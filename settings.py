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
    'yuras007@ukr.net',
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^c)!y#yitssh7b%4gyge-_l!5py*cc8&tin0$%jx^x1%$36ji='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['lykartest.com']

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

#Email settings
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#ADMINS = (
#    ('admin', 'yuras007@ukr.net'),   # email will be sent to your_email
#)
#MANAGERS = ADMINS
#DEFAULT_FROM_EMAIL = 'webmaster@localhost'
#MANAGERS = (
#    'geo.savchuk@gmail.com',
#    'hyralmisha@gmail.com',
#)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social.apps.django_app.default',
    'easy_thumbnails',
    'crispy_forms',

    'apps.home',
    'apps.accounts',
    'apps.internal',

    'apps.contacts',

    'captcha',

    'apps.polls',


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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lykarcom_db',
        'USER': 'root',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static-collect/')
STATIC_ROOT = '/home/lykarcom/domains/lykar.com.ua/public_html/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

STATIC_URL = '/static/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_ROOT = '/home/lykarcom/domains/lykar.com.ua/public_html/media/'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures/'),
)

AUTH_PROFILE_MODULE = 'apps.accounts.UserProfile'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
#    'social.backends.twitter.TwitterOAuth',
    'social.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

#social settings
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_FACEBOOK_KEY = '794744153918111'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f9eae78ca2a90f2e9de78cef5c1735fc'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    # pattern is (source key, destination key)
    ('email', 'email'),
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '662075687340-5tibn1gh9tiu00road2s9uf7rltml4js.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Zd-LZGPavPa2tdMoCMWVt2el'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', ]
SOCIAL_AUTH_GOOGLE_EXTRA_DATA = [
    # pattern is (source key, destination key)
    ('email', 'email'),
]

#SOCIAL_AUTH_TWITTER_KEY = 'qPa17vMyGZk0MpnjLeFK474pP'
#SOCIAL_AUTH_TWITTER_SECRET = 'owWb9CFbwoHKU6zc9KWKiPemfSIlfwDs8pwoUFGVwNrXsbJgPk'

SOCIAL_AUTH_VK_OAUTH2_KEY = '4619476'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '55n826lBeD3FLcyBazD8'
SOCIAL_AUTH_VK_APP_USER_MODE = 0
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email', 'photos', ]
SOCIAL_AUTH_VK_EXTRA_DATA = [  # configure how the data is labelled on SocialAuth.extra_data
    # pattern is (source key, destination key)
    ('email', 'email'), ('photos', 'photos'),
]



SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'apps.accounts.pipeline.get_profile_picture',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

try:
    from local_settings import *
except ImportError:
    pass
