from datetime import timedelta
from flaskr.utils import rand_str
from flaskr.config import getenv


class Development:
    DEBUG = True
    SECRET_KEY = rand_str(64)
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
