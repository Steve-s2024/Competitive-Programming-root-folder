# ABC445 D, seems impossible at first, but then the greedy solution I come up with is just genius
from collections import defaultdict, deque, Counter
from typing import List
from heapq import heapify, heappush, heappop
from sortedcontainers import SortedList
from math import gcd, lcm, inf, sqrt, floor, ceil, comb
from functools import cache
from sys import stdout, setrecursionlimit
from itertools import permutations
from bisect import bisect_left, bisect_right



def solve():
    H ,W, n = [int(e) for e in input().split()]
    hmp = {}
    wmp = {}
    mp = defaultdict(list)
    for i in range(n):
        h, w = [int(e) for e in input().split()]
        if h not in hmp: hmp[h] = defaultdict(int)
        if w not in wmp: wmp[w] = defaultdict(int)
        hmp[h][w] += 1
        wmp[w][h] += 1
        mp[(h, w)].append(i)

    x, y = 0, 0
    ans = []
    while len(ans) < n:
        if H in hmp:
            for k, v in hmp[H].items():
                for _ in range(v):
                    if len(ans) >= n: break
                    ans.append((x, y, mp[(H, k)].pop()))
                    W, x = W-k, x+k
                    wmp[k][H] -= 1
                    if wmp[k][H] == 0: wmp[k].pop(H)
        if W in wmp:
            for k, v in wmp[W].items():
                for _ in range(v):
                    if len(ans) >= n: break
                    ans.append((x, y, mp[(k, W)].pop()))
                    H, y = H-k, y+k
                    hmp[k][W] -= 1
                    if hmp[k][W] == 0: hmp[k].pop(W)

    # print(ans)
    # print(ans)
    ANS = [None]*n
    for x, y, i in ans: ANS[i] = (y, x)
    # print(ANS)
    for i in range(n): print(' '.join(str(e+1) for e in ANS[i]))




solve()