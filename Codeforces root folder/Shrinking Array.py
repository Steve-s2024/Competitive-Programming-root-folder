# a load of my shoulder... harder than the average B in div.2
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    inf = math.inf
    n = int(input())
    nums = [int(e) for e in input().split()]
    res = inf
    mp1 = {}
    stk = []
    for i in range(n):
        while stk and nums[i] >= stk[-1][1]-1:
            idx, num = stk.pop()
            mp1[idx] = i
        stk.append((i, nums[i]))
    mp2 = {}
    stk = []
    for i in range(n):
        while stk and nums[i] <= stk[-1][1]+1:
            idx, num = stk.pop()
            mp2[idx] = i
        stk.append((i, nums[i]))

    for i in range(n):
        if i in mp1 and i in mp2: res = min(res, max(mp1[i], mp2[i])-i-1)

    mp1 = {}
    stk = []
    for i in range(n-1, -1, -1):
        while stk and nums[i] >= stk[-1][1] - 1:
            idx, num = stk.pop()
            mp1[idx] = i
        stk.append((i, nums[i]))
    mp2 = {}
    stk = []
    for i in range(n-1, -1, -1):
        while stk and nums[i] <= stk[-1][1] + 1:
            idx, num = stk.pop()
            mp2[idx] = i
        stk.append((i, nums[i]))

    for i in range(n):
        if i in mp1 and i in mp2: res = min(res, i-min(mp1[i], mp2[i])-1)


    if res == inf: print(-1)
    else: print(res)


t = int(input())
for i in range(t):
    solve()


# TLE
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    inf = math.inf
    n = int(input())
    nums = [int(e) for e in input().split()]
    res = inf
    for i in range(n):
        x = nums[i]
        mi, mx = inf, -inf
        for j in range(i+1, n):
            mi, mx = min(mi, nums[j]), max(mx, nums[j])
            if x in range(mi, mx+1) or x-1 in range(mi, mx+1) or x+1 in range(mi, mx+1):
                res = min(res, j-i-1)
                break

    for i in range(n-1, -1, -1):
        x = nums[i]
        mi, mx = inf, -inf
        for j in range(i-1, -1, -1):
            mi, mx = min(mi, nums[j]), max(mx, nums[j])
            if x in range(mi, mx+1) or x-1 in range(mi, mx+1) or x+1 in range(mi, mx+1):
                res = min(res, i-j-1)
                break

    if res == inf: print(-1)
    else: print(res)


t = int(input())
for i in range(t):
    solve()