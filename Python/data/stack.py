import sys
from traceback import format_exc


def main():
    print(f'test: {None}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
