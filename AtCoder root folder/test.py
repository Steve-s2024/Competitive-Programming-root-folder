from collections import defaultdict, deque, Counter
import heapq, math
from math import sqrt, inf, ceil
from linecache import cache
from decimal import Decimal, getcontext




def solve():
    n, m, l = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    arr = [e%m for e in arr]
    # print(arr)

    dp = {}
    def recursive(i, remain):
        state = (i, remain)
        if state in dp: return dp[state]
        if i >= l:  return 0 if remain == 0 else inf

        res = inf
        for j in range(remain+1):
            tot = i
            arr[i] += j
            for k in range(i+l, n, l):
                dist = abs(arr[i]-arr[k])
                cnt = dist//m
                d1, d2 = cnt*m, (cnt+1)*m
                tot += min(abs(d1-dist), abs(d2-dist))

            arr[i] -= j
            a = recursive(i+1, remain-j)
            res = min(res, a + tot)
        dp[state] = res
        print(state)
        print(res)
        return res

    sm = sum(arr[:l])
    # print(ceil(sm/m)*m - sm)
    res = recursive(0, ceil(sm/m)*m - sm)
    print(res)

solve()