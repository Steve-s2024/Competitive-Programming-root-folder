# disgusting problem
def solve():
    n, m, k = [int(e) for e in input().split()]
    l, r = k-1, n-k
    res = 0
    for i in range(1, min(l, r)+1):
        if i+(i-1) + i <= m: res = i
    l -= res
    r -= res
    cst = res+(res-1) + res
    m -= cst
    res *= 2
    while l and m >= 2:
        m -= 2
        res += 1
        l -= 1
    while r and m >= 2:
        m -= 2
        res += 1
        r -= 1
    print(res+1)

'''def solve():
    n, m, k = [int(e) for e in input().split()]

    l, r = k, k
    x = 1
    res = 0
    f, g = 0, 0
    while m and r-l+1 < n:
        a, b = k-l, r-k
        if not (m > a and l-1) and not (m > b and n-r):
            res = min(f-g, m//2)
            break

        if m > a and l-1:
            f = l-1
            mi = min(m-a, x, l-1)
            # mi -> max number of fortify to left
            l -= mi
            t = mi+a
            x = t
            m -= t
            g = mi

        if m > b and n-r:
            f = n-r
            mi = min(m-b, x, n-r)
            # mi -> max number of fortify to right
            r += mi
            t = mi+b
            x = t
            m -= t
            g = mi

    print(min(n, r-l+1 + res))'''

for _ in range(int(input())): solve()

