from collections import defaultdict, deque, Counter
import heapq, math
from math import sqrt, inf
from linecache import cache
from decimal import Decimal, getcontext



# tle
def solve():
    n = int(input())
    prr, arr, brr = [], [], []
    for i in range(n):
        p, a, b = [int(e) for e in input().split()]
        prr.append(p)
        arr.append(a)
        brr.append(b)


    pre = []
    tot = 0
    for i in range(n):
        tot += brr[i]
        pre.append(tot)

    mp = {}
    def recursive(i, x):
        nonlocal n, mp
        state = (i, x)
        if state in mp: return mp[state]
        if i >= n: return x
        if prr[i] < x:
            x -= min(x, brr[i])
        else:
            x += arr[i]
        mp[state] = recursive(i + 1, x)
        return mp[state]

    # tle caused by this loop
    q = int(input())
    mx = max(prr)
    for i in range(q):
        x = int(input())
        l, r = 0, n-1
        res = 0
        while l <= r:
            m = (l+r)//2
            if x - pre[m] <= mx:
                res = m
                r = m-1
            else: l = m+1
        if not x <= mx: x -= min(x, pre[res])
        else: res = -1

        print(recursive(res+1, x))

solve()