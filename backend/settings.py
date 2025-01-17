import os
from pathlib import Path
import sys
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h(35e6h29f%nz=(3jaa(c_q-e=nk@y+3!ubsvs@efc#y##4g*p"
    
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    'mozilla_django_oidc',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework_simplejwt',
    'departemen',
    'django_extensions',
    'divisi',
    'jabatan',
    'profile',
    'lampiran',
    'surat',
    'klasifikasi',
    'group',
    'drf_yasg',
    'djongo',
    'pymongo',
    'corsheaders',
    'storages'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "NAME": os.environ.get("DB_NAME", "ndecoffis"),
	'CLIENT': {
                'host': os.environ.get("DB_HOST", "127.0.0.1"),
                'port': os.environ.get("DB_PORT", 27017),
        },
    }
}

if os.environ.get("DB_USE_AUTH"):
    DATABASES['default']['CLIENT'].update({
                'username': os.environ.get("DB_USERNAME", "admin"),
                'password': os.environ.get("DB_PASSWORD", "admin"),
                'authSource': os.environ.get("DB_AUTHSOURCE", "$external"),
                'authMechanism': os.environ.get("DB_AUTHMECHANISM", "SCRAM-SHA-1"),
    })


REST_FRAMEWORK = {
    # "EXCEPTION_HANDLER": "apps.common.exceptions.common_exception_handler",
    # "NON_FIELD_ERRORS_KEY": "error",
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #            'common.authbackends.XAuthUser',
    # ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_RENDERER_CLASSES": ("apps.api.renderers.GlobalJSONRenderer",),
    # "EXCEPTION_HANDLER": "apps.api.exceptions.common_exception_handler",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

AUTHENTICATION_BACKENDS = [ 
        "django.contrib.auth.backends.ModelBackend",
        "mozilla_django_oidc.auth.OIDCAuthenticationBackend"
]
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = os.environ.get("STATIC_URL", "static/")
MEDIA_URL = os.environ.get("MEDIA_URL", "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

OIDC_RP_CLIENT_ID = os.environ.get('OIDC_RP_CLIENT_ID', "nde")
OIDC_RP_CLIENT_SECRET = os.environ.get('OIDC_RP_CLIENT_SECRET', "CPeUriP0S9kGlQ56cQdtgBW6DzDSUDkv")
OIDC_BASE_URL = os.environ.get("OIDC_BASE_URL","https://newsso.coofis.com")
OIDC_REALMS = os.environ.get("OIDC_REALMS", "coofis")
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{OIDC_BASE_URL}/realms/{OIDC_REALMS}/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{OIDC_BASE_URL}/realms/{OIDC_REALMS}/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{OIDC_BASE_URL}/realms/{OIDC_REALMS}/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{OIDC_BASE_URL}/realms/{OIDC_REALMS}/protocol/openid-connect/certs"
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_CREATE_USER = False

LOGIN_REDIRECT_URL = os.environ.get("LOGIN_REDIRECT_URL", "/api/auth/extoken")

if os.environ.get("USE_MINIO"):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_ACCESS_KEY_ID = os.environ.get("MINIO_KEY", "minioadmin")
    AWS_SECRET_ACCESS_KEY = os.environ.get("MINIO_SECRET", "miniopassword")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("MINIO_BUCKET", "coofis")
    AWS_S3_ENDPOINT_URL = os.environ.get("MINIO_URL", "https://localhost/9000")  # Ganti dengan endpoint MinIO Anda
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
