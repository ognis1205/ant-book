from datetime import timedelta
from flaskr.config.utils import getenv, randstr


class Development:
    DEBUG = True
    SECRET_KEY = randstr(64)
    JWT_SECRET_KEY = randstr(64)
    SESSION_COOKIE_SECURE = False,
    SESSION_COOKIE_HTTPONLY = False,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    BCRYPT_LOG_ROUNDS = 4
