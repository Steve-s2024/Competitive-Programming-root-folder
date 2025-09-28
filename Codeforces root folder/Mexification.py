# boring question
from collections import defaultdict, deque, Counter
import heapq
from math import inf, gcd, lcm, sqrt
from linecache import cache
import sys


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    st = set(nums)
    mex = -1
    for i in range(n):
        if i not in st:
            mex = i
            break

    if mex == -1:
        print(sum(nums))
        return

    mp = Counter(nums)
    mi = inf
    for i in range(n):
        num = nums[i]
        if mp[num] == 1:
            if nums[i] > mex: mi = min(mi, nums[i])
            nums[i] = min(num, mex)
        else:
            mi = min(mi, nums[i])
            nums[i] = mex

    if k == 1:
        print(sum(nums))
        return
    k -= 2

    st = set(nums)
    mex2 = -1
    for i in range(n):
        if i not in st:
            mex2 = i
            break

    if mex2 == -1:
        print(sum(nums))
        return

    # print(nums)
    if mi < mex:
        for i in range(n): nums[i] = min(nums[i], mi)
        mex = max(nums)+1
        # print(1, nums)
        if k%2 == 0: print(sum(nums))
        else:
            for i in range(n):
                if nums[i] == mex-1: nums[i] = mex
            print(sum(nums))
    else:
        for i in range(n):
            if nums[i] == mex: nums[i] = mex+1
        # print(2, nums)
        if k%2 == 0: print(sum(nums))
        else:
            for i in range(n):
                if nums[i] == mex+1: nums[i] = mex
            print(sum(nums))


t = int(input())
for i in range(t):
    solve()