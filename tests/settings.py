DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django_etuovi",
)

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

SITE_ID = 1
DEBUG = True
USE_TZ = True
SECRET_KEY = "xxx"
LANGUAGES = (("fi", "Finnish"), ("en", "English"), ("sv", "Swedish"))
