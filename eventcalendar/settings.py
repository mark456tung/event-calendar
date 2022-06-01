"""
Django settings for eventcalendar project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from telnetlib import AUTHENTICATION

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "i8e1s3!_(fjsiv%1pn3sb3o=s)!p*nzwh1$gp5-l&%nb!d=y_s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "calendarapp.apps.CalendarappConfig",
    "accounts.apps.AccountsConfig",
    #allauth 
    #'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # line provider 
    'allauth.socialaccount.providers.line',
    'LineBot'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "eventcalendar.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "eventcalendar.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation." "MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation." "CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation." "NumericPasswordValidator"},
]

AUTH_USER_MODEL = "accounts.User"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*.jp.ngrok.io']


#line login setting
AUTHENTICATION_BACKEND = (
    'django.contrib.auth.backend.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 2

SOCIALACCOUNT_PROVIDERS = {
          'line': {
              'APP': {
                   'client_id': '1657152198',
                  'secret': 'c27e1c6fdc361607383f37c4b1b68cdf'
              },
              "SCOPE": ['profile', 'openid', 'email']
          }
      }

# LOGIN_REDIRECT_URL = '/calendar/'
LINE_CHANNEL_ACCESS_TOKEN = 'o4pPo44PZkj7z8TCZbo3CDBTWPrSx8Ls+PJrovx7SBZMmpBp0hTInlK5Q8i4UPjAAbg24RRA6Am46GFAKJ42kGeNtcsPMKdVBFo1Bz/YJyNZwiEQn3vzgWhOq56TR7en6PeFVctJMKwKUOjLjndtdAdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = 'd1cee8bb03b7b550fd2eccdafb1e55c6'
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*.jp.ngrok.io']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False