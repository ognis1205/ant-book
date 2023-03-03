import sys
from traceback import format_exc


def main(size):
    line, acc, w = '', [], 4 * size - 3
    for i in reversed(range(size)):
        c, l = chr(ord('a') + i), len(line)
        line = line[:l//2+1] + c + line[l//2:]
        acc.append('-'.join(line).center(w, '-'))
    print('\n'.join(acc))
    print('\n'.join(reversed(acc[:-1])))


if __name__ == '__main__':
    try:
        main(int(input()))
    except:
        print(format_exc(), file=sys.stderr)
