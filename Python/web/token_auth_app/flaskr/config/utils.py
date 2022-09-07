import os
from random import choice
from string import printable
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent / '.env')


def getenv(key, default=None):
    return os.getenv(key, default=default)


def getconf(key):
    return {
        'dev': 'flaskr.config.development.Development',
        'test': 'flaskr.config.testing.Testing',
        'prod': 'flaskr.config.production.Production',
    }.get(key, 'flaskr.config.development.Development')


def randstr(length):
    return ''.join([choice(printable) for _ in range(length)])
