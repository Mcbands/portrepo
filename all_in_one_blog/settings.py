import os
from pathlib import Path
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(5cy_99cnmxe$bqab%c^_5fg#1a1+*v9qe^et!z+fpkwpf=4%s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog_app",
    "crispy_forms",
    "crispy_bootstrap4",
    'ckeditor',
    'ckeditor_uploader',
    'portfolio',

]

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar': 'full',
        'removePlugins':'exportpdf',
        'extraPlugins': ','.join(
            [
                'codesnippet','widget','html5video','youtube'
                
            ]
        ),       
    }
}





MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "all_in_one_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog_app.context_processors.get_categories",
            ],
        },
    },
]




WSGI_APPLICATION = "all_in_one_blog.wsgi.application"



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'your_email_password'  # Replace with your Gmail password or App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER








# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True




# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'fpgr@ph1xx@gmail.com'  # Your Gmail address
# EMAIL_HOST_PASSWORD ='gwxx yfvw bxgp ajiy'  # The 16-character App Password you generated
EMAIL_HOST_USER = 'bandasevier010@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD ='Fpgr@ph1xx'  # The 16-character App Password you generated
# Optional: Set the default 'from' email address
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CRISPY_TEMPLATE_PACK = "bootstrap4"
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
LOGIN_URL = "/account/login"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
