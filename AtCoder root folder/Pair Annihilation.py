# can't believe I solved this challenging E in half an hour left
# it is absolutely non-typical style question, and I have to go through
# a lot of thinking and failed before finally realize the greedy solution
# it shows my reasoning ability, the greedy here is elegant
import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(100000000)


def solve():
    n = int(input())
    x = [int(e) for e in input().split()]
    graph = defaultdict(list)
    for i in range(n-1):
        u, v, w = [int(e) for e in input().split()]
        graph[u].append((v, w))
        graph[v].append((u, w))

    vis = set()
    eng = 0
    def dfs(node):
        nonlocal eng

        tot = 0
        for nxt, wei in graph[node]:
            if nxt in vis:
                continue
            vis.add(nxt)
            a = dfs(nxt)
            tot += a
            eng += wei * abs(a)

        return tot + x[node-1]
    vis.add(1)
    dfs(1)
    print(eng)

# t = int(input())
t = 1
for i in range(t):
    solve()

