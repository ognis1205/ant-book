def lps(patt):
    l, ret = 0, [0] * len(patt)
    for i in range(1, len(patt)):
        if patt[i] == patt[l]:
            l += 1
            ret[i] = l
        else:
            l = 0
    return ret


def kmp(text, patt):
    table = lps(patt)
    i, j, ret = 0, 0, []
    while i < len(text):
        if text[i] == patt[j]:
            i, j = i + 1, j + 1
            if j == len(patt):
                ret.append(i - j)
                j = table[j - 1]
        elif j == 0:
            i += 1
        else:
            j = table[j]
    return ret


if __name__ == '__main__':
    text, patt = input(), input()
    print(text, patt)
    print(kmp(text, patt))
    text, patt = input(), input()
    print(text, patt)
    print(kmp(text, patt))
