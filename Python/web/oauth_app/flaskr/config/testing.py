from datetime import timedelta
from flaskr.config.utils import getenv, rand_str


class Testing:
    DEBUG = True
    SERVER_NAME = 'localhost:5000'
    SECRET_KEY = rand_str(64)
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
