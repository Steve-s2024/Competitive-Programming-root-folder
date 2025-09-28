from collections import defaultdict, deque, Counter
import heapq, math
from math import sqrt, inf, ceil
from linecache import cache
from decimal import Decimal, getcontext



def solve(mod):
    mod = 10 ** 9 + 7
    n = int(input())
    nums = [int(e) for e in input().split()]
    res = 1
    cnt = 1
    for num in nums:
        for i in range(1, num+1):
            res *= cnt
            res %= mod
            res *= pow(i, mod-2, mod)
            res %= mod
            cnt += 1
    print(res)



t, m = [int(e) for e in input().split()]
for i in range(t):
    solve(m)


