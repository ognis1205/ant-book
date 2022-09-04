from datetime import timedelta
from flaskr.config.utils import get_env, rand_str


class Production:
    DEBUG = False
    SECRET_KEY = rand_str(64)
    SQLALCHEMY_DATABASE_URI = get_env('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
