from collections import defaultdict, deque, Counter
from typing import List
from heapq import heapify, heappush, heappop
# from sortedcontainers import SortedList
from math import gcd, lcm, inf, sqrt, floor, ceil, comb, factorial
from functools import cache
from sys import stdout, setrecursionlimit
from itertools import permutations
from bisect import bisect_left, bisect_right
from time import time
from random import randint



def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    sm = sum(nums)
    if sm%n != 0:
        print('No')
        return

    avg = sm//n

    mp = [0]*50
    for e in nums:
        if e == avg: continue
        x = 1
        while x <= e and (avg-(e-x)).bit_count() != 1:
            x <<= 1

        if x > e or avg-(e-x) <= 0 or (avg-(e-x)).bit_count() != 1:
            print('No')
            return

        a, b = x, avg-(e-x)
        print(a, b)

        a, b = a.bit_length(), b.bit_length()
        mp[a] += 1
        mp[b] -= 1


    for e in mp:
        if e != 0:
            print('No')
            return

    print('Yes')


for _ in range(int(input())): solve()

