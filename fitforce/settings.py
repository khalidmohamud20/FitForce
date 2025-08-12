import os
from pathlib import Path
import dj_database_url

# --------------------
# BASE SETTINGS
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Set up environment variable for DATABASE_URL
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_rNuQ9lohms3M@ep-solitary-voice-a2yoqhyt.eu-central-1.aws.neon.tech/fled_wad_dairy_66815"
)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-fallback-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    '127.0.0.1,localhost,.herokuapp.com'
).split(',')

# --------------------
# INSTALLED APPS
# --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'workouts',  # Your app
]

# --------------------
# MIDDLEWARE
# --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Enable WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitforce.urls'

# --------------------
# TEMPLATES
# --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'workouts' / 'templates'],
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

WSGI_APPLICATION = 'fitforce.wsgi.application'

# --------------------
# DATABASE
# --------------------
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL") or f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# --------------------
# PASSWORD VALIDATORS
# --------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------
# INTERNATIONALIZATION
# --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------
# STATIC FILES
# --------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Local static files
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Where collectstatic puts files

# WhiteNoise storage backend for hashed & compressed static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --------------------
# MEDIA FILES (if needed later)
# --------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------
# DEFAULT PK TYPE
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------
# LOGIN SETTINGS
# --------------------
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

# --------------------
# PRODUCTION SECURITY
# --------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
