from flaskr.config.getenv import getenv
from flaskr.config.development import Development


def getconf(key):
    return {
        'dev':  'flaskr.config.Development',
        'test': 'flaskr.config.Testing',
        'prod': 'flaskr.config.Production',
    }.get(key, 'flaskr.config.Development')


__all__ = [
    "getenv",
    "getconf",
    "Development",
]
