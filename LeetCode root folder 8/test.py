from collections import defaultdict, deque, Counter
from typing import List
from sortedcontainers import SortedList
from heapq import heapify, heappush, heappop
from math import gcd, lcm, inf, sqrt
from functools import cache


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10 ** 9 + 7

        m = r - l + 1
        arr = [(1, 1)] * m
        for i in range(n):
            tmp = [(0, 0)] * n
            abv = 0
            blw = sum(e[0] for e in arr)
            for j in range(m):
                tmp[j][0] += abv
                abv += arr[j][1]
                blw -= arr[j][0]
                tmp[j][1] += blw
            arr = tmp

        res = sum(e[0] for e in arr) - arr[-1][1] + sum(e[1] for e in arr) - arr[0][0]
        return res % mod

