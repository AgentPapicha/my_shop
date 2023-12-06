"""
Django settings for my_shop project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
# import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# env = environ.Env(
#     DEBUG=(bool, False)
# )
#
# environ.Env.read_env(env_file=BASE_DIR.joinpath('.env').open(encoding='UTF-8'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2=88$48p0ono-&34vnd=iqocdo1)8(1v)cn_#3cj1z)yg4$d@7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

STRIPE_SECRET_KEY = 'sk_test_51O9tIsJcK0ecXttYzovqExTj9YMtSL0Gl9jGRv1i0fjnGQwnFHfHd3VXRHWRst5UWOVU6F4VXomZKSV2RMYg0K1n004W6YYH54'

STRIPE_PUBLISHABLE_KEY ='pk_test_51O9tIsJcK0ecXttYZWpFHyQlMlMOz6JjFKVnNttjQeTT1TxthKdHxWrJdpF1JKCTvXUesNxwghH1sUmUnwKqcUKL00IC7BMnYy'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_shop',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'products',
    'order',
    'blog',
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
#     "HEAD"
# )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100
}

ROOT_URLCONF = 'my_shop.urls'

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

WSGI_APPLICATION = 'my_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#
# DATABASES = {
#
#     'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'USER': 'shop_admin',
#             'PASSWORD': 'pasha2109',
#             'NAME': 'shop_database',
#             'PORT': '5432',
#         }
#
# }

# for docker
DATABASES = {

    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': [
         'rest_framework.authentication.TokenAuthentication',
         'rest_framework.authentication.BasicAuthentication',
         'rest_framework.authentication.SessionAuthentication',
     ]
 }

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

