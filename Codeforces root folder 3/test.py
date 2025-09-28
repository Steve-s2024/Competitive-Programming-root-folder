from collections import defaultdict, deque, Counter
from math import inf, ceil, floor, sqrt, gcd, lcm
import heapq, math
import sys

sys.setrecursionlimit(100000000)



def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    mp = [nums[:]]
    pw = 2
    while pw <= n:
        tmp = []
        for i in range(0, n - pw + 1): tmp.append(max(mp[-1][i], mp[-1][i + pw // 2]))
        mp.append(tmp)
        pw *= 2

    res = 0
    for i in range(m):
        l, r = [int(e) for e in input().split()]
        l, r = l-1, r-1
        if r-l < 2:
            res += 1
            continue
        l = l+1
        r = r-1
        sz = r - l + 1
        ln = sz.bit_length()
        opt = max(mp[ln - 1][l], mp[ln - 1][r - pow(2, ln - 1) + 1])
        if opt <= nums[l-1]: res += 1
    print(res)

t = int(input())
for i in range(t):
    solve()