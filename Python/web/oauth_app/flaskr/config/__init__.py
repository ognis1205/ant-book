from flaskr.config.getenv import getenv
from flaskr.config.development import Development


def getconf(key):
    return {
        'development':  'flaskr.config.Development',
        'testing': 'flaskr.config.Testing',
        'production': 'flaskr.config.Production',
    }.get(key, 'flaskr.config.Development')


__all__ = [
    "getenv",
    "getconf",
    "Development",
]
