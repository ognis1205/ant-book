from string import printable
from random import choice


def rand_str(length):
    return ''.join([choice(printable) for _ in range(length)])
