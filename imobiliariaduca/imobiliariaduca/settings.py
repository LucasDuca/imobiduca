# coding: utf-8
"""
Django settings for imobiliariaduca project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rdl6=re10%tyalcehbkn2p)8fc$x2dmta37=^mc0zmlwc0rf0v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

MEDIA_URL = "/static/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'etc/public/static/media/')
STATIC_URL = "/static/collect/"
STATIC_ROOT = os.path.join(BASE_DIR, 'etc/public/static/collect/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'etc/public/static/'),]

ALLOWED_HOSTS = []

NOME_CLIENTE = 'ImobiDuca'
DESCRICAO = 'Site da imobiliária Duca'
AUTOR = 'Lucas Duca'
COPYRIGHT = 'Copyright © ImobiDuca 2017'



LOGIN_REDIRECT_URL = '/cliente/'
LOGIN_URL = '/cliente/login/'
LOGOUT_URL = '/cliente/logout/'

# Application definition


#SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
#SPATIALITE_LIBRARY_PATH='/usr/local/lib/mod_spatialite.dylib'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    #minhas
    'base',
    'cliente',
    'imovel',
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

ROOT_URLCONF = 'urls.urls'

WSGI_APPLICATION = 'imobiliariaduca.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#gettext = lambda s: s


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_CONTEXT_PROCESSORS += ('base.context_processors.geral', )