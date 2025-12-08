# tle on TC23...

from heapq import heappop, heappush


def solve():
    n, m = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    for i in range(m):
        s, t, w = [int(e) for e in input().split()]
        s, t = s-1, t-1
        g[s].append((t, w))

    vis = [0]*n
    minheap = [(0, 0, brr[0])]
    while minheap:
        mx, u, bat = heappop(minheap)
        vis[u] = bat
        if u == n-1:
            print(mx)
            return

        for v, w in g[u]:
            if bat >= w and bat+brr[v] > vis[v]:
                heappush(minheap, (max(mx, w), v, bat+brr[v]))

    print(-1)

t = int(input())
for i in range(t): solve()




