"""
Django settings for recepy_book project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import django_heroku
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-weemh=mhn2^==kixissnbpy0&07#i2uv+_k4ux3i(-q8n*^76r'
SECRET_KEY = os.environ.get('SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
DEBUG = False

# ALLOWED_HOSTS = ['recipe-book-2023.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = ['*']

LOGIN_URL = '/login'
# LOGIN_REDIRECT_URL = '/main'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_panel',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recepy_book.urls'

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

WSGI_APPLICATION = 'recepy_book.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
# 	'default': {
#       	'ENGINE': 'django.db.backends.postgresql',
#       	'HOST' : os.environ.get('POSTGRES_HOST', 'localhost'),
#       	'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
#       	'USER': os.environ.get('POSTGRES_USER', 'username'),
#       	'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
#       	'PORT': os.environ.get('POSTGRES_PORT', '5432'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC_URL = 'admin_panel/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = []


# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '../static'),
# )
# django_heroku.settings(locals())

ON_HEROKU = os.environ.get('ON_HEROKU')
HEROKU_SERVER = os.environ.get('HEROKU_SERVER')
if ON_HEROKU:
    DATABASE_URL = 'postgresql://<postgresql>'
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
