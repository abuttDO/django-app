"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import sys
import dj_database_url
from django.core.management.utils import get_random_secret_key
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,159.203.76.97").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA URL IS FOR POINTING TO THE DATABASE SAVED FILES
##MEDIA_URL = '/media/'
##MEDIA_ROOT = os.path.join(BASE_DIR, "static")

##STATIC_URL = "/static/"
##STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

##STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
##STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

##### SPACES STORAGE CONFIGURATIONS
AWS_ACCESS_KEY_ID = os.environ.get("SPACES_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("SPACES_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("BUCKET_NAME")
AWS_REGION_NAME = os.environ.get("SPACES_REGION")  # something like "nyc3"
AWS_S3_ENDPOINT_URL = 'https://%s.digitaloceanspaces.com' % AWS_REGION_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
########### LINKEDIN TUTORIAL SITE CODE ################
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'portfolio.custom_storages.StaticStorage'
STATIC_URL = '%s/%s/' % (AWS_S3_ENDPOINT_URL, STATICFILES_LOCATION)


MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'portfolio.custom_storages.MediaStorage'
MEDIA_URL = '%s/%s/' % (AWS_S3_ENDPOINT_URL, 'media')
########################################################

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'jobs/static'),
#]
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#MEDIAFILES_DIRS = [
#    os.path.join(BASE_DIR, 'jobs/media'),
#]

#MEDIAFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

###################################


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    from .local_settings import *
except ImportError:
    pass
