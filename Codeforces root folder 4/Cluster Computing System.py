# greedy very much
from collections import defaultdict, deque, Counter
from typing import List
from heapq import heapify, heappush, heappop
# from sortedcontainers import SortedList
from math import gcd, lcm, inf, sqrt, floor, ceil, comb
from functools import cache
from sys import stdout, setrecursionlimit
from itertools import permutations
from bisect import bisect_left, bisect_right



class gcdTable():
    def __init__(self, nums):
        n, sp, pw = len(nums), [nums[:]], 2
        while pw <= n:
            tmp = []
            for i in range(0, n - pw + 1): tmp.append(gcd(sp[-1][i], sp[-1][i + pw // 2]))
            sp.append(tmp)
            pw *= 2
        self.sp = sp

    def query(self, l, r):
        sp, ln = self.sp, (r - l + 1).bit_length()
        return gcd(sp[ln - 1][l], sp[ln - 1][r - pow(2, ln - 1) + 1])


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    # n = 5
    # nums = [2, 2, 6, 3, 3]
    gcdt = gcdTable(nums)
    res = gcdt.query(0, n-1)
    for i in range(1, n-1):
        # print(i, gcdt.query(0, i), gcdt.query(i, n-1))
        res += min(gcdt.query(0, i), gcdt.query(i, n-1))
    print(res)


solve()