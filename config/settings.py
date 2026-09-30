# IMPORTING STANDARD PACKAGES
import os

# IMPORTING KLAARYO PACKAGES
from mini_kit.settings import REST_FRAMEWORK  # noqa: F401

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "rest_framework",
    "mini_kit",
    "django_db_models.apps.DjangoDbModelsConfig",
    "rest_apis.apps.RestApisConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
APPEND_SLASH = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "applications"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

MINI_KIT_JWT_SECRET = os.getenv("MINI_KIT_JWT_SECRET", "dev-only-mini-kit-secret-at-least-32-bytes")
