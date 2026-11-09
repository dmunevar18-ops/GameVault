
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SEGURIDAD

SECRET_KEY = 'CONSERVA_AQUI_TU_SECRET_KEY_ACTUAL'

DEBUG = True

ALLOWED_HOSTS = []


# APLICACIONES INSTALADAS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'catalogo',
]


# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# CONFIGURACIÓN DE URLS

ROOT_URLCONF = 'gamevault.urls'


# PLANTILLAS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# APLICACIÓN WSGI

WSGI_APPLICATION = 'gamevault.wsgi.application'


# BASE DE DATOS SQLITE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# VALIDACIÓN DE CONTRASEÑAS

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


# INTERNACIONALIZACIÓN

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# ARCHIVOS ESTÁTICOS (CSS, JAVASCRIPT)

STATIC_URL = 'static/'


# ARCHIVOS MULTIMEDIA (FOTOGRAFÍAS)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# REDIRECCIONES DE AUTENTICACIÓN

LOGIN_REDIRECT_URL = 'inicio'

LOGOUT_REDIRECT_URL = 'inicio'

LOGIN_URL = 'login'


# CLAVE PRIMARIA POR DEFECTO

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
