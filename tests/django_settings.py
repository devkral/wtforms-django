from django.conf.global_settings import *


INSTALLED_APPS = ["tests", "wtforms_django"]
# Django 1.0 to 1.3
DATABASE_ENGINE = "sqlite3"
TEST_DATABASE_NAME = ":memory:"
# Django 1.4+
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]
