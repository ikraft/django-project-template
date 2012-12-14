# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *

PROJECT_NAME = '{{ project_name }}'
PROJECT_DOMAIN = '127.0.0.1:8000'
PROJECT_URL = 'http://' + PROJECT_DOMAIN

import os
import string
import random

DEBUG = False
TEMPLATE_DEBUG = DEBUG

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here('..', '..')
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Etc/UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = root('uploads')
MEDIA_URL = '/static/uploads/'
STATIC_ROOT = root('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    root('assets'),
)
STATICFILES_FINDERS += (
)
SECRET_KEY = 'h^v06=u4-b@s-!5*xh&amp;j9=c9$g6$@u0rv+x5ilb%)r$(knj8)u'

TEMPLATE_LOADERS += (
)
MIDDLEWARE_CLASSES += (
)
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
TEMPLATE_DIRS = (
        root('templates'),
)
SITE_ID = 1
INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Third Party Apps
    #'south',
    #'social_auth',
    #'compressor',

    # Internal Apps

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTOLOAD_TEMPLATETAGS = (
    'compressor.templatetags.compress',
)
