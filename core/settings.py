"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from decouple import config
import dj_database_url


def get_env_variable(name, cast=str, default=""):
    try:
        return cast(os.environ[name])
    # pylint: disable=W0702, bare-except
    except:
        return config(name, cast=cast, default=default)


BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = get_env_variable("DEBUG", cast=bool)
ENVIRONMENT = get_env_variable("ENVIRONMENT", default="development")

mailjet_api_key = get_env_variable("MAILJET_API_KEY")
mailjet_api_secret = get_env_variable("MAILJET_API_SECRET")

DEFAULT_FROM_EMAIL = "contact@apilos.beta.gouv.fr"

if mailjet_api_key != "":
    EMAIL_BACKEND = "django_mailjet.backends.MailjetBackend"
    MAILJET_API_KEY = mailjet_api_key
    MAILJET_API_SECRET = mailjet_api_secret
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CONVERTAPI_SECRET = get_env_variable("CONVERTAPI_SECRET")

env_allowed_hosts = []
try:
    env_allowed_hosts = os.environ["ALLOWED_HOSTS"].split(",")
except KeyError:
    pass

ALLOWED_HOSTS = ["localhost"] + env_allowed_hosts

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "bailleurs.apps.BailleursConfig",
    "conventions.apps.ConventionsConfig",
    "instructeurs.apps.InstructeursConfig",
    "programmes.apps.ProgrammesConfig",
    "stats.apps.StatsConfig",
    "users.apps.UsersConfig",
    "upload.apps.UploadConfig",
    "comments.apps.CommentsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": False,
            "context_processors": [
                "core.context_processor.get_environment",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


try:
    database_url = os.environ["DATABASE_URL"]
    default_settings = dj_database_url.config()
except KeyError:
    default_settings = {
        "ENGINE": "django.db.backends.postgresql",
        "USER": config("DB_USER"),
        "NAME": config("DB_NAME"),
        "HOST": config("DB_HOST"),
        "PASSWORD": config("DB_PASSWORD"),
        "PORT": config("DB_PORT", default="5432"),
        "TEST": {
            "NAME": config("DB_NAME") + "-test",
        },
        "ATOMIC_REQUESTS": True,
    }

DATABASES = {"default": default_settings}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Why STAGING = FALSE ?
STAGING = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

# Redirect to home URL after login
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Object storage with Scaleway
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = get_env_variable("AWS_DEFAULT_ACL")
AWS_S3_REGION_NAME = get_env_variable("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = get_env_variable("AWS_S3_ENDPOINT_URL")

if AWS_ACCESS_KEY_ID:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Security settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Lax"

# https://django-csp.readthedocs.io/en/latest/configuration.html
CSP_DEFAULT_SRC = "'none'"
CSP_SCRIPT_SRC = ("https://stats.data.gouv.fr/piwik.js",)
# CSP_SCRIPT_SRC_ELEM = ("https://stats.data.gouv.fr/piwik.js",)  # Matomo
CSP_IMG_SRC = ("'self'", "data:")
CSP_OBJECT_SRC = "'none'"
CSP_FONT_SRC = "'self'", "data:"
CSP_CONNECT_SRC = ("'self'", "https://stats.data.gouv.fr/piwik.php")
CSP_STYLE_SRC = "'self'"
CSP_MANIFEST_SRC = "'self'"
CSP_INCLUDE_NONCE_IN = [
    "script-src",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
