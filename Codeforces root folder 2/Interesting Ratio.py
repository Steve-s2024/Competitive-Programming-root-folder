# this is the best way I can think of, maybe try it with
# c++: TLE

def solve():
    n = int(input())
    primes = []
    cands = [i for i in range(2, n+1)]
    while cands:
        m = len(cands)
        primes.append(cands[0])
        tmp = []
        for i in range(1, m):
            if cands[i] % cands[0] != 0:
                tmp.append(cands[i])
        cands = tmp

    # print(primes)
    res = 0
    for p in primes:
        res += n // p
    print(res)

t = int(input())
for tt in range(t):
    solve()