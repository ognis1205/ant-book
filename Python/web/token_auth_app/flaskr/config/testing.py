from datetime import timedelta
from flaskr.config.utils import getenv, randstr


class Testing:
    DEBUG = True
    SECRET_KEY = randstr(64)
    SESSION_COOKIE_SECURE = False,
    SESSION_COOKIE_HTTPONLY = False,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
