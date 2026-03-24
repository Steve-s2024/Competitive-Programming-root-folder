# im just the type of genius that surprise myself from time to time.
# trying to figure out the modular inverse relation here, but unfortunately it only applies if m can evenly divide n
# instead, I am thinking in the other way, way not treat it as n % p, where p = m*mod. and at the end divide the remainder
# by m. tbh, did not think this could work so well. need to analyze the modular property hidden here.

def solve():
    k, m = [int(e) for e in input().split()]

    M = 10007*m
    ref = [1]
    x = 1
    l = 1
    for _ in range(30):
        x = (x * pow(10, l, M) + x) % M
        ref.append(x)
        l *= 2
    pw = [10]
    x = 10
    for _ in range(29):
        x = (x * x) % M
        pw.append(x)

    x = 0
    for _ in range(k):
        c, l = [int(e) for e in input().split()]
        x *= pow(10, l, M)
        p = 1
        for i in range(31):
            if 1<<i & l:
                x = (x + ref[i]*p*c)%M
                p = (p*pw[i])%M
    # print(x)
    print(x//m)
solve()