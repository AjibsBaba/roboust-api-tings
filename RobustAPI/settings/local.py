from .base import *

DEBUG = bool(os.getenv('DA_STATUS'))

ALLOWED_HOSTS = ['*']

# Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
