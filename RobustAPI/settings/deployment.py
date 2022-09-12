import dj_database_url

from .base import *

DEBUG = bool(os.getenv('DA_STATUS'))
ALLOWED_HOSTS = []

DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
