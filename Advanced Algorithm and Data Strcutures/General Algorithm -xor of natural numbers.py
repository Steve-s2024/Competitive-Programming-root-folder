# provide logn time to compute the result of 1^2^3...^(n-1)^n

def xorN(n):
    s = str(bin(n))[2:]
    sz = len(s)
    res = [0] * sz
    for i in range(sz):
        a, b = (int(s[:i], 2) if i else 0), (int(s[i + 1:], 2) if i < sz - 1 else 0)
        if s[i] == '1':
            res[i] = a * 2 ** (sz - i - 1) + b + 1
        else:
            res[i] = a * 2 ** (sz - i - 1)

    # return res   res contains the number of 1 bit in each spot
    return int(''.join(str(e%2) for e in res), 2)


# the sequence follows obvious pattern... this algorithm will be replaced by constant algo that manipulate such discovery
for i in range(1, 1000):
    print(xorN(i))
