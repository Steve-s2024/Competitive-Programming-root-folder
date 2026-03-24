# kinda interesting graph problem. work that bipartite graph
# 2026/03/16 div2 D

def solve():
    n, m = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)

    res = 0
    mp = [0]*n
    vs = [0]*n
    for u in range(n):
        if vs[u]: continue
        vs[u] = 1
        q = deque([u])
        f = 1
        bi = True
        a, b = 0, 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if mp[u] == 0: a += 1
                else: b += 1
                for v in g[u]:
                    if not vs[v]:
                        vs[v] = 1
                        mp[v] = f
                        q.append(v)
                    bi = bi and mp[v] != mp[u]
            f = (f+1)%2
        if bi: res += max(a, b)
    print(res)

for _ in range(int(input())): solve()

