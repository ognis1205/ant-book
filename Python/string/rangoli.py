import sys
from traceback import format_exc


def main():
    s = int(input())
    line, acc, w = '', [], 4 * s - 3
    for i in reversed(range(s)):
        c, l = chr(ord('a') + i), len(line)
        line = line[:l//2+1] + c + line[l//2:]
        acc.append('-'.join(line).center(w, '-'))
    print('\n'.join(acc))
    acc = reversed(acc[:-1])
    print('\n'.join(acc))

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
