import sys
from traceback import format_exc


class my_repeat:
    def __init__(self, value):
        self._value = value

    def __next__(self):
        return self._value


def my_zip_longest(*args, fillvalue=None):
    iters = [iter(arg) for arg in args]
    num_active = len(args)
    while True:
        ret = []
        for i, it in enumerate(iters):
            try:
                v = next(it)
                ret.append(v)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iters[i] = my_repeat(fillvalue)
                ret.append(fillvalue)
        yield ret


def main():
    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd', 'e', 'f']
    c = []
    for x in my_zip_longest(a, b, c):
        print(f'test: {x}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
