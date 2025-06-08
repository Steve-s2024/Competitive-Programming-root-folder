import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(100000000)

import sys

sys.setrecursionlimit(1 << 20)  # Increase recursion limit for deep trees


def solve():
    N = int(input())
    x = [int(e) for e in input().split()]
    tree = defaultdict(list)

    for _ in range(N - 1):
        u, v, w = [int(e) for e in input().split()]
        tree[u].append((v, w))
        tree[v].append((u, w))

    total_cost = 0

    def dfs(u, parent):
        nonlocal total_cost
        net_charge = x[u]

        for v, w in tree[u]:
            if v == parent:
                continue
            child_charge = dfs(v, u)
            total_cost += abs(child_charge) * w
            net_charge += child_charge

        return net_charge

    dfs(0, -1)
    print(total_cost)


solve()