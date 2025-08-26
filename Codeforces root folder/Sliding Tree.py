# at least I tried. today I made record to possibly be in top 1000th in a div2 contest
# all I did was solved the first three questions superfast. performance goated, very likely due to the cold environment
# help me produces some adrenaline. early the contest my heart rate is pretty high, mind is a bit muffled.

from collections import defaultdict, deque, Counter
import heapq
from math import inf, gcd, lcm, sqrt
from linecache import cache
import sys


def solve():
    n = int(input())
    graph = defaultdict(list)
    deg = [0]*n
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        deg[u-1] += 1
        deg[v-1] += 1
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    vis = set()
    mp = [0]*n
    def dfs(node):
        for nxt in graph[node]:
            if nxt in vis: continue
            vis.add(nxt)
            mp[node] += dfs(nxt)
        return mp[node] + 1
    mx, idx = -1, -1
    for i in range(n):
        if deg[i] > mx:
            mx = deg[i]
            idx = i
    if mx <= 2:
        print(-1)
        return

    vis.add(idx)
    dfs(idx)

    mx, mi = -inf, inf
    i1, i2 = -1, -1
    for nei in graph[idx]:
        if mp[nei] > mx:
            i1 = nei
            mx = mp[nei]
        if mp[nei] < mi:
            i2 = nei
            mi = mp[nei]

    res = [i1, idx, i2]
    print(' '.join(str(e+1) for e in res))



t = int(input())
for i in range(t):
    solve()
