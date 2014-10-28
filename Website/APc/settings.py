# Django settings for blog project.
import os
APP_DIR = os.path.dirname( globals()['__file__'] )
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
this_directory = os.path.dirname(__file__)

DBNAME = 'components'


STATICFILES_DIRS = (
    BASE_DIR + '/static/',  # or project_static, whatever
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request",
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-vu%up9720#wny@my&jf47bwd07l(l025jk&en!)mjb%m-ttui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pcbuilder',
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

ROOT_URLCONF = 'APc.urls'

WSGI_APPLICATION = 'APc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # How to format the output
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        },

    # Log handlers (where to go)
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
            },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': this_directory + "/log.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
            },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': this_directory + "/celery.log",
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        },
        },

    # Loggers (where does the log come from)
    'loggers': {
        'repackager': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
            },
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
            },
        'django.db.backends': {
            'handlers': ['console', 'logfile'],
            'level': 'WARN',
            'propagate': False,
            },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['logfile'],
            'propagate': True,
            },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['logfile'],
            'propagate': False,
            },
        'celery': {
            'handlers': ['celery'],
            'level': 'DEBUG',
            },
        }
}