import os
import string
from datetime import timedelta
from dotenv import load_dotenv
from flaskr.utils import rand_str


load_dotenv(override=True)


class Development:
    DEBUG = True
    #SECRET_KEY=os.getenv('SECRET_KEY')
    SECRET_KEY = rand_str(64)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
