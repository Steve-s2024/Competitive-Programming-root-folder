# when using a defaultdict as the dp, TLE on 26th... optimized it to using array (which is not easy to notice it is
# achievable) it passed
from collections import deque, Counter, defaultdict


def solve():
    mod = 998244353
    n = int(input())
    p = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    for i, e in enumerate(p): g[e-1].append(i+1)

    mp = [[0]]
    q = deque([0])
    while q:
        mp.append([])
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                q.append(v)
                mp[-1].append(v)
    mp.pop()
    # for r in mp: print(r)

    dp = [0]*n
    for u in mp[-1]: dp[u] = 1
    sm = sum(dp)
    for i in range(len(mp)-2, -1, -1):
        tmp = 0
        for u in mp[i]:
            dp[u] = sm+1
            if i == 0: continue
            for v in g[u]: dp[u] -= dp[v]
            tmp += dp[u]
            tmp %= mod
        sm = tmp

        # print(dp)
    print(dp[0]%mod)

t = int(input())
for i in range(t):
    solve()
