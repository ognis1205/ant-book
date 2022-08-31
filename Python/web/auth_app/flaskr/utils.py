import string
from random import choice


def rand_str(length):
    return "".join(
        [choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&') for i in range(length)]
    )
