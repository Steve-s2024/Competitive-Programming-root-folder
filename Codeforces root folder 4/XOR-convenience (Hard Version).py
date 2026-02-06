# this is pure gamble, I solved easy version greedily, and added some sauce to spice it up
# the solution guarantee to find valid answer if n is not power of 2
# the solution return -1 if n is power of 2.
# turns out it worked, if n is power of 2 then no valid solution can exist
def solve():
    n = int(input())

    p = [0]*n
    p[-1] = 1
    for i in range(n-2, 0, -1): p[i] = (i+1)^1
    st = set(p)
    for i in range(2, n+1):
        if i not in st: p[0] = i
    # print(p)
    if n%2 == 0 and p[0] == n:
        mp = {}
        for i in range(n): mp[p[i]] = i
        for i in range(2, n):
            j = n^i
            if j > n: continue
            if i < mp[j]:
                p[0], p[i] = p[i], p[0]
                break
        else:
            print(-1)
            return
        print(' '.join(str(e) for e in p))
    else: print(' '.join(str(e) for e in p))


for _ in range(int(input())): solve()