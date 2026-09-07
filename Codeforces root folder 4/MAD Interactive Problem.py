# 3n solution
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




def query(ar):
    if len(ar) < 2: return 0
    k = len(ar)
    print(f'? {k} {' '.join(str(e+1) for e in ar)}')
    stdout.flush_stdout()
    res = int(input())
    if res == -1: exit(4399)
    return res





def solve():

    n = int(input())

    res = [0]*(2*n)
    ar = [0]
    for i in range(1, 2*n):
        ar.append(i)
        x = query(ar)
        if x:
            res[i] = x
            ar.pop()

    ar = [2*n-1]
    for i in range(2*n-2, -1, -1):
        ar.append(i)
        if res[i]: continue
        x = query(ar)
        if x:
            res[i] = x
            ar.pop()

    # print(res)

    print(f'! {' '.join(str(e) for e in res)}')

for _ in range(int(input())): solve()



# time wise workable, but exceed 3n query limit

def query(ar):
    if len(ar) < 2: return 0
    k = len(ar)
    print(f'? {k} {' '.join(str(e+1) for e in ar)}')
    stdout.flush_stdout()
    res = int(input())
    if res == -1: exit(4399)
    return res


def bs(l, r, vs, x):
    R = r
    res = -1
    while l <= r:
        m = (l+r) // 2
        ar = []
        for i in range(m, R+1):
            if vs[i] == 0: ar.append(i)
        if query(ar) >= x:
            res = m
            l = m+1
        else: r = m-1
    return res


def solve():
    n = int(input())
    vs = [0]*(2*n)

    for i in range(n):
        l, r = 0, 2*n-1
        res, c = -1, -1
        while l <= r:
            # if i: print('Yes')
            m = (l+r)//2
            ar = []
            for j in range(m+1):
                if vs[j] == 0: ar.append(j)
            # if i: print('Yes', ar)
            tp = query(ar)
            if tp:
                res, c = m, tp
                r = m-1
            else: l = m+1

        res2 = bs(0, res, vs, c)
        vs[res] = vs[res2] = c
    print(f'! {' '.join(map(str, vs))}')


for _ in range(int(input())): solve()