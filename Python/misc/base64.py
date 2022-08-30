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
    return ''.join([padding(ord(c)) for c in seq])


def to_quartet(seq):
    ret = []
    while len(seq) > 0:
        b, seq = seq[:6], seq[6:]
        ret.append(NUM2CHAR[int(b, 2)])
    ret = ''.join(ret) + '=' * ((4 - (len(ret) % 4)) % 4)
    return ret


def encode(s):
    return to_quartet(to_bin(s))


if __name__ == '__main__':
    print(encode('ABCDEFG'))
