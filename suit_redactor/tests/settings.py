# Django settings for testproject project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = True

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3",}}

TIME_ZONE = "Europe/Riga"
LANGUAGE_CODE = "en-uk"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ""
MEDIA_URL = ""
SECRET_KEY = "vaO4Y<g#YRWG8;Md8noiLp>.w(w~q_b=|1`?9<x>0KxA%UB!63"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "suit_redactor.tests.urls"
TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "suit_redactor",
    "django.contrib.admin",
)

STATIC_URL = "/static/"
