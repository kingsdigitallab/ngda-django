from .base import *  # noqa

INTERNAL_IPS = INTERNAL_IPS + ['']
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_ngda_liv',
        'USER': 'app_ngda',
        'PASSWORD': '',
        'HOST': ''
    },
}
