"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'SECRET_KEY', '$f!wm1042d+aa&hch6n6lfhifb)n%w%cn^of-gyi7^n73y*j5o')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'TRUE').upper() == 'TRUE'

ALLOWED_HOSTS = []

EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    
    # 3rd party
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'django_q',
    
    # our apps
    'apps.test_one'
]

SITE_ID = 1

#! Fill this after getting all info for allAuth lib, setting for every providers
SOCIALACCOUNT_PROVIDERS = { 
    # 'google': {
    #     'SCOPE': [
    #         'profile',
    #         'email',
    #     ],
    #     'AUTH_PARAMS': {
    #         'access_type': 'online',
    #     }
    # },
    # "apple": {
    #     "APP": {
    #         # Your service identifier.
    #         "client_id": "your.service.id",

    #         # The Key ID (visible in the "View Key Details" page).
    #         "secret": "KEYID",

    #          # Member ID/App ID Prefix -- you can find it below your name
    #          # at the top right corner of the page, or it’s your App ID
    #          # Prefix in your App ID.
    #         "key": "MEMAPPIDPREFIX",

    #         # The certificate you downloaded when generating the key.
    #         "certificate_key": """-----BEGIN PRIVATE KEY-----
    #         s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
    #         3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
    #         c3ts3cr3t
    #         -----END PRIVATE KEY-----
    #         """
    #     }
    # },'facebook': {
    #     'METHOD': 'oauth2',
    #     'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
    #     'SCOPE': ['email', 'public_profile'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'first_name',
    #         'last_name',
    #         'middle_name',
    #         'name',
    #         'name_format',
    #         'picture',
    #         'short_name'
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC': 'path.to.callable',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v7.0',
    # }
}



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

# WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_DEFAULT_NAME','app'),
        'USER': os.getenv('DB_DEFAULT_USER','app'),
        'PASSWORD': os.getenv('DB_DEFAULT_PASSWORD','app'),
        'HOST': os.getenv('DB_DEFAULT_HOST', 'db_default'),
        'PORT': '5432',
    },
    'djangoq': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_DJANGOQ_NAME','app'),
        'USER': os.getenv('DB_DJANGOQ_USER','app'),
        'PASSWORD': os.getenv('DB_DJANGOQ_PASSWORD','app'),
        'HOST': os.getenv('DB_DEFAULT_HOST', 'db_djangoq'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS =[
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'djangoq'
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'db_memcached:11211',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000"
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    #   r"^https://\w+\.example\.com$",
]

CORS_ALLOW_ALL_ORIGINS = os.getenv('CORS_ALLOW_ALL_ORIGINS', 'TRUE').upper() == 'TRUE'

try:
    from .local_settings import *
except ImportError:
    pass
