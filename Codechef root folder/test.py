from collections import defaultdict, deque, Counter
from typing import List
import heapq, sys
from math import gcd, lcm, inf, sqrt
from functools import cache
sys.setrecursionlimit(1 << 20)

n = 100
vis = set()
minheap = [(0, 1, 0)]
while minheap:
    _, node, par = heapq.heappop(minheap)
    if node in vis: continue
    vis.add(node)
    print(f'{str(bin(par))[2:].zfill(8)} --> {str(bin(node))[2:].zfill(8)}')
    # print(f'{par} --> {node}')
    for cand in range(1, n+1):
        if cand not in vis:
            heapq.heappush(minheap, (cand^node, cand, node))







# def solve():
#     n = int(input())
#
#
#
#
# t = int(input())
# for i in range(t):
#     solve()

