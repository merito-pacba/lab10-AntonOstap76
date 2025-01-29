import os
from .settings import *
from .settings import BASE_DIR

# Security settings
SECRET_KEY = os.environ['SECRET']  # Set the SECRET_KEY as an environment variable
DEBUG = True

ALLOWED_HOSTS = ["stiven-bobs-ajd7a7hqekguhtak.polandcentral-01.azurewebsites.net"]

CSRF_TRUSTED_ORIGINS = [
    "https://stiven-bobs-ajd7a7hqekguhtak.polandcentral-01.azurewebsites.net"
]


# Middleware configuration with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory where `collectstatic` will store files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Use WhiteNoise for optimized static files


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session storage
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Additional settings
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'