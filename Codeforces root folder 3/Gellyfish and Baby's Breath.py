# highest rank ever after solve this question: 826th in a live contest

import sys
sys.setrecursionlimit(10000000)

def getPow(p, b, MOD):
    tmp = b
    res = 1
    while p:
        re = p%2
        if re:
            res *= tmp
            res %= MOD
        tmp *= tmp
        tmp %= MOD
        p >>= 1
    return res



def solve():
    MOD = 998244353
    n = int(input())
    p = [int(e) for e in input().split()]
    q = [int(e) for e in input().split()]

    res = []
    mx1, mx2 = [0, p[0]], [0, q[0]]
    for i in range(n):
        if p[i] > mx1[1]:
            mx1 = (i, p[i])
        if q[i] > mx2[1]:
            mx2 = (i, q[i])

        if mx1[1] > mx2[1]:
            res.append((mx1[1], q[i-mx1[0]]))
        elif mx2[1] > mx1[1]:
            res.append((mx2[1], p[i-mx2[0]]))
        else:
            if q[i-mx1[0]] > p[i-mx2[0]]:
                res.append((mx1[1], q[i-mx1[0]]))
            else:
                res.append((mx2[1], p[i-mx2[0]]))

    # print(res)
    ans = []
    for a, b in res:
        tot = getPow(a, 2, MOD) + getPow(b, 2, MOD)
        ans.append(tot%MOD)
    # print(ans)
    print(' '.join(str(e) for e in ans))
t = int(input())
for i in range(t):
    solve()

