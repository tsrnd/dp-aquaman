"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url
from dotenv import load_dotenv
import datetime
from rest_framework.settings import APISettings

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == 'True'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'yashoes',
    'yashoes_frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('CACHE_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AUTH_USER_MODEL = 'yashoes.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.IsAuthenticated', ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER':
    'yashoes.helper.custom_jwt.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
    'yashoes.helper.custom_jwt.jwt_get_username_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_SECRET_KEY':
    SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY':
    None,
    'JWT_ALGORITHM':
    'HS256',
    'JWT_VERIFY':
    True,
    'JWT_VERIFY_EXPIRATION':
    True,
    'JWT_LEEWAY':
    0,
    'JWT_EXPIRATION_DELTA':
    datetime.timedelta(days=3),
    'JWT_AUDIENCE':
    'team4+team1',
    'JWT_ISSUER':
    'team4+team1',
    'JWT_ALLOW_REFRESH':
    True,
    'JWT_REFRESH_EXPIRATION_DELTA':
    datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX':
    'Bearer',
}


### configuration frontend, and admin
import yashoes_frontend, yashoes
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(yashoes_frontend.__file__), "share/templates/"),
            os.path.join(os.path.dirname(yashoes.__file__), "templates/")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(yashoes_frontend.__file__), "share/static/"),
]

MINIO_SERVER = os.getenv('STORAGE_URL')
MINIO_ACCESSKEY = 'AKIAIOSFODNN7EDAMPLP'
MINIO_SECRET = 'wJalrXUtnFEMKJH7MDENJFTPxRfiCYEXAMPLEKEY'
MINIO_BUCKET = 'mybucket'
MINIO_SECURE = False
DEFAULT_FILE_STORAGE = 'yashoes.helper.custom_minio_storage.CustomMinioStorage'

API_HOST = 'http://localhost:8000/'

# SESSION_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
