import os

BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../doctor/db.sqlite3'),
    }
}