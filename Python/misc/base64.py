import sys
from traceback import format_exc


NUM2CHAR = (
    r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r'abcdefghijklmnopqrstuvwxyz'
    r'0123456789+/'
)

CHAR2NUM = dict(zip(NUM2CHAR, range(len(NUM2CHAR))))


def to_bin(seq):
    def padding(o):
        if o <= int('7F', 16):
            return bin(o)[2:].rjust(8, '0')
        return bin(o)[2:]
    ret = ''.join([padding(ord(c)) for c in seq])
    return ret + '0' * ((6 - (len(ret) % 6)) % 6)


def to_quartet(seq):
    ret = []
    while len(seq) > 0:
        b, seq = seq[:6], seq[6:]
        ret.append(NUM2CHAR[int(b, 2)])
    return ''.join(ret) + '=' * ((4 - (len(ret) % 4)) % 4)


def encode(string):
    return to_quartet(to_bin(string))


def from_quartet(seq):
    ns = []
    for c in seq:
        if c == '=': break
        try: ns.append(CHAR2NUM[c])
        except: pass
    return ''.join([bin(n)[2:].rjust(6, '0') for n in ns])


def from_bin(seq):
    ret = []
    while len(seq) >= 8:
        if seq.startswith('1111'):
            b, seq = seq[:32], seq[32:]
        elif seq.startswith('1110'):
            b, seq = seq[:24], seq[24:]
        elif seq.startswith('1100'):
            b, seq = seq[:16], seq[16:]
        else:
            b, seq = seq[:8], seq[8:]
        ret.append(chr(int(b, 2)))
    return ''.join(ret)


def decode(base64):
    return from_bin(from_quartet(base64))


def main():
    test = 'ABCDEFG'
    print(f'input: {test}')
    base64 = encode(test)
    print(f'encoded: {base64}')
    string = decode(base64)
    print(f'decoded: {string}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
