from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'le8w-r7fb1-16zq0ilw=ml+r0vp0^ut&3xz26n%ym0njk1dxj5' # Cambia esto por una clave segura en producción

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  


ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] 
LANGUAGES = [
    ('es', 'Español'),
    ('en', 'English'),
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # <- Necesario
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <- Necesario
    'django.contrib.messages.middleware.MessageMiddleware', # <- Necesario
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hydro_wells.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hydro_wells_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        },
    }
}

# Para ver correos en consola (desarrollo)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Para producción, descomenta y configura uno real:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'tu-contraseña-o-app-password'
# DEFAULT_FROM_EMAIL = 'HydroWells <noreply@hydrowells.com>'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files (uploads from admin)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Zona horaria
# Para Estados Unidos (Maryland), usar 'America/New_York'
# O puedes usar 'UTC' si prefieres
TIME_ZONE = 'America/New_York'


# Formato de fecha y hora
USE_L10N = True
USE_I18N = True
# Desactivar el soporte de zonas horarias de Django
USE_TZ = False

# Mantener una zona horaria base (opcional, pero recomendado)
TIME_ZONE = 'America/New_York' # O 'UTC'