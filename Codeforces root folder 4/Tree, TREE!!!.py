# despicable memory limit! forcing me to turn dfs into iterative loop...

def solve():
    n, k = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)

    mp = {}
    vs = set()
    x = 0
    def dfs(u):
        nonlocal x
        res = 1
        for v in g[u]:
            if v in vs: continue
            vs.add(v)
            res += dfs(v)
        if res >= k: x += 1
        mp[u] = res
        return res
    vs.add(0)
    dfs(0)

    # print(x)
    vs = set()
    ans = 0
    def recursive(u, x):
        nonlocal ans, n
        ans += x
        for v in g[u]:
            if v in vs: continue
            vs.add(v)
            a, b = 0, 0
            if n >= k and n-mp[v] < k: a = 1
            if mp[v] < k and n >= k: b = 1
            # print(a, b)
            recursive(v, x-a+b)

    vs.add(0)
    recursive(0, x)
    print(ans)

for _ in range(int(input())): solve()

