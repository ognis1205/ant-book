import sys
from traceback import format_exc


def main():
    print('success')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), f=sys.stderr)
