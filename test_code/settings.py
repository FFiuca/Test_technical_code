"""
Django settings for test_code project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%*f(b15j(yer4+hlp(o-#yx9ov)_-ek)&_cudv&!_&8)uysj2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app_main',

    "rest_framework",
    "django_extensions",
    "corsheaders",
]

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

ROOT_URLCONF = 'test_code.urls'

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

WSGI_APPLICATION = 'test_code.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True


REST_FRAMEWORK  = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', # this module neeede for default auth djano, in section is django temporray login and logout
        'rest_framework.authentication.TokenAuthentication', # way to know avaible auth type: open https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme and rest_xxx.autxxx.{List of APIReference}
    ],
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated', # any route who access must login
        'rest_framework.permissions.AllowAny',
    ],
    # https://www.django-rest-framework.org/api-guide/throttling/
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10000/day', # test for login view
    #     'user': '10000/day',
    #     'login-attempt' : '2/minute', # look user_app.throttling.LoginThrottle
    #     'register-attempt' : '10/minute',
    # },
    # 'TEST_REQUEST_RENDERER_CLASSES': [
    #     # 'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     # 'rest_framework.renderers.TemplateHTMLRenderer'
    # ]

    # for default setting on generic and viewset view, if want on APIView to apply see https://stackoverflow.com/questions/35830779/django-rest-framework-apiview-pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', # "next": "http://127.0.0.1:8000/watch/stream/review/filter/?limit=4&offset=4&username=admin",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?cursor=cD0yMDIzLTA3LTIzKzA4JTNBMTIlM0E0Mi44NTg2NzYlMkIwMCUzQTAw&username=admin
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?page=2&username=admin
    # 'PAGE_SIZE': 4
}
