# it is so annoyed that they make F easier than E, and the solve count doesn't indicate that. fortunately I determined
# to skip E and do it regardless of the adversity.

def solve():
    n, m = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    st = set()
    for _ in range(m):
        u, v = [int(e) for e in input().split()]
        if (u, v) in st or u == v: continue
        st.add((u, v))
        u, v = u-1, v-1
        g[u].append(v)

    vs2 = [0]*n
    i = 0
    ans = [inf]*n
    vs = [0]*n
    vs[0] = 1
    hp = [0]
    mx = -1
    while hp:
        u = heappop(hp)
        mx = max(mx, u)
        vs2[u] = 1
        while i < n and vs2[i]: i += 1


        for v in g[u]:
            if vs[v]: continue
            vs[v] = 1
            heappush(hp, v)
        # print(u, i)
        # if i-1 == u: ans[u] = len(hp)
        if vs[i-1] and mx == i-1: ans[i-1] = min(ans[i-1], len(hp))
    # print(ans)
    for i in range(n):
        if ans[i] == inf: ans[i] = -1
    for v in ans: print(v)

solve()