from pathlib import Path
import os

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность
SECRET_KEY = 'django-insecure-f@zw)8ss@@hmp%xv-by^^8*a3vn&x+h^-zc8fe8#)uv$0gp^us'
DEBUG = True
ALLOWED_HOSTS = []

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'weather',
    'debug_toolbar',  # Для отладки
]

# Middleware
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Debug Toolbar первым!
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'coolsite.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Для кастомной админки и форм
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

# WSGI
WSGI_APPLICATION = 'coolsite.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Проверка паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статика
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),
]

# Медиа (изображения)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Кэширование (файловое)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'coolsite_cache'),
    }
}

# Редиректы
LOGIN_REDIRECT_URL = '/weather/'        # После входа
LOGOUT_REDIRECT_URL = '/weather/login/' # После выхода

# Debug Toolbar (ограничен локальным IP)
INTERNAL_IPS = [
    "127.0.0.1",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
