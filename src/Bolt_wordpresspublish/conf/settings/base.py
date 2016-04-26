"""
Django settings for monstrocity.

For more information on this file, see
https://docs.djangoproject_name.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject_name.com/en/1.7/ref/settings/
"""

# Build paths inside the project_name like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os.path import dirname, abspath, basename, join, normpath

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        if default is None:
            error_msg = "Set the %s env variable" % setting
            raise ImproperlyConfigured(error_msg)
        else:
            return default


SITE_ROOT = dirname(dirname(dirname(abspath(__file__))))
SITE_NAME = basename(SITE_ROOT)
sys.path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings.local")

ADMINS = (('Wai Keat', 'waikeat.wong@gmail.com'),)
MANAGERS = ADMINS

FROM_EMAIL = 'hello@bolttest.com'
DEFAULT_FROM_EMAIL = 'hello@bolttest.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject_name.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$116+l@v+w3q)w--v+yxp&ba5r-@=z&oza7-yhyv6c6a=y@eci'


ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'django_wysiwyg',
    'ckeditor',
)

LOCAL_APPS = (
    'bolt_website',
    'bolt_user',
    'bolt_usersite',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
)

# Database
# https://docs.djangoproject_name.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': get_env_setting('bolttest_DB_NAME',
                                'bolt_test'),
        }
}

# Internationalization
# https://docs.djangoproject_name.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-sg'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Login/Logout Url

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject_name.com/en/1.7/howto/static-files/

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

LOCALE_PATHS = (
    normpath(join(SITE_ROOT, 'locale')),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

DJANGO_TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

THIRD_PARTY_CONTEXT_PROCESSORS = (
)

LOCAL_CONTEXT_PROCESSORS = (
)

TEMPLATES[0]['OPTIONS']['context_processors'] = \
    DJANGO_TEMPLATE_CONTEXT_PROCESSORS + THIRD_PARTY_CONTEXT_PROCESSORS + LOCAL_CONTEXT_PROCESSORS

AUTH_USER_MODEL = 'bolt_user.BoltUser'

DJANGO_WYSIWYG_FLAVOR = 'ckeditor'
