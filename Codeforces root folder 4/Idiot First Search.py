# codeforces is really forcing me to do iterative DFS...
def solve():
    mod = 10**9 + 7
    n = int(input())
    g = [[] for _ in range(n+1)]
    g[0] = [1]
    for u in range(1, n+1):
        l, r = [int(e) for e in input().split()]
        if l: g[u] = [l, r]
    mp = [0]*(n+1)
    # def dfs(u):
    #     res = 0
    #     for v in g[u]:
    #         res += dfs(v)+2
    #         res %= mod
    #     mp[u] = res
    #     return res
    # dfs(0)

    stk = [0]
    vs = [0]*(n+1)
    while stk:
        o = len(stk)
        u = stk[-1]
        if vs[u] == 0:
            vs[u] = 1
            for v in g[u]: stk.append(v)
        if len(stk) == o:
            stk.pop()
            if g[u]:
                for v in g[u]: mp[u] += mp[v]+2
    mp[0] = 0
    # print(mp)



    ans = [0]*(n+1)
    # def fn(u, sm, d):
    #     ans[u] = (sm+d+mp[u])%mod
    #     for v in g[u]: fn(v, (sm+mp[u])%mod, d+1)
    # fn(0, 0, 0)

    stk = [(0, 0, 0)]
    while stk:
        u, sm, d = stk.pop()
        ans[u] = (sm + d + mp[u]) % mod
        for v in g[u]: stk.append((v, (sm+mp[u])%mod, d+1))

    # print(ans[1:])
    print(' '.join(str(e) for e in ans[1:]))





for _ in range(int(input())): solve()




