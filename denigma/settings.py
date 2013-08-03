"""
Django settings for destiny project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)
print(PACKAGE_ROOT)
print(BASE_DIR == PACKAGE_ROOT)

# Import template context processors:
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '82qt$#33#^^#oyq@gh2d5%)m1@aqn))1%d3))$v2oyl2b5^r-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition


default = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles']

theme = ['pinax_theme_bootstrap_account', 'pinax_theme_bootstrap', 'django_forms_bootstrap']
external = ['account','metron', 'eventlog']
useful =   ['json_field','south']

project = ['utils']
rest = ['rest_framework','rest_framework_swagger', 'django_filters']
#useful =   ['south']

compilers = ['coffeescript', 'less']
    


INSTALLED_APPS = default+theme+external+useful+project+rest+compilers


TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'pinax_utils.context_processors.settings',
    'account.context_processors.account',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'denigma.urls'

WSGI_APPLICATION = 'denigma.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = ('static',)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(PACKAGE_ROOT, 'templates')]


# Required?

SITE_ID = 1

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
THEME_ACCOUNT_ADMIN_URL = True

AUTHENTICATION_BACKENDS = [
    'account.auth_backends.UsernameAuthenticationBackend',
]
