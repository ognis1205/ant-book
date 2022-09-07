from datetime import timedelta
from flaskr.config.utils import getenv, randstr


class Production:
    DEBUG = True
    SECRET_KEY = randstr(64)
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
