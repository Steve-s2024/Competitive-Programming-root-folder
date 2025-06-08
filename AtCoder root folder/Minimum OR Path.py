# couldn't get this done on time, wasted too much on D

import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(100000000)

def solve():
    n, m = [int(e) for e in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        u, v, w = [int(e) for e in input().split()]
        graph[u].append((v, w))
        graph[v].append((u, w))

    vis = set()
    dp = {}
    def dfs(node):
        nonlocal n
        if node in dp:
            return dp[node]
        if node == n:
            return 0
        mi = float('inf')
        for nxt, wei in graph[node]:
            if nxt not in vis:
                vis.add(nxt)

                a = dfs(nxt)
                if a != float('inf'):
                    mi = min(a|wei, mi)
                vis.remove(nxt)
        dp[node] = mi
        return mi
    vis.add(1)
    print(dfs(1))




# t = int(input())
t = 1
for i in range(t):
    solve()

