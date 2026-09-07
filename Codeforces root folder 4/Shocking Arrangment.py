# okey dokey greedy greedy
from collections import defaultdict, deque, Counter
from typing import List
from heapq import heapify, heappush, heappop
# from sortedcontainers import SortedList
from math import gcd, lcm, inf, sqrt, floor, ceil, comb
from functools import cache
from sys import stdout, setrecursionlimit
from itertools import permutations
from bisect import bisect_left, bisect_right



def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    k = max(nums) - min(nums)

    nums.sort()
    res = [nums[0]]
    l, r = 1, n-1
    sm = nums[0]
    ans = [nums[0]]
    while l <= r:
        if sm < 0:
            sm += nums[r]
            ans.append(nums[r])
            r -= 1
        else:
            sm += nums[l]
            ans.append(nums[l])
            l += 1
        res.append(sm)
    # print(res)
    if max(res)-min(res) >= k:
        print('No')
        return
    print('Yes')
    print(' '.join(str(e) for e in ans))


for _ in range(int(input())): solve()
