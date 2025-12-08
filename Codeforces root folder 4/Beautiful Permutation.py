# just need to know the definition a := a+1 for all a in range [l, r]
# we can easily know the right end using this fact and the fact we know left end
from functools import cache
from math import inf
from sys import stdout
from random import randint
from collections import deque, Counter, defaultdict
from heapq import heappop, heappush

# [int(e) for e in input().split()]

def query(typ, l, r):
    print(f'{typ} {l+1} {r+1}')
    stdout.flush()
    return int(input())


def solve():
    n = int(input())

    l, r = 0, n-1
    a = -1
    while l <= r:
        m = (l+r)//2
        if query(1, l, m) != query(2, l, m):
            a = m
            r = m-1
        else: l = m+1

    b = a + (query(2, a, n-1) - query(1, a, n-1)) - 1
    print(f'! {a+1} {b+1}')


t = int(input())
for i in range(t): solve()

# can't make query less than 40...

from sys import stdout

def query(typ, l, r):
    print(f'{typ} {l+1} {r+1}')
    stdout.flush()
    return int(input())


def solve():
    n = int(input())

    l, r = 0, n-1
    a = -1
    while l <= r:
        m = (l+r)//2
        if query(1, l, m) != query(2, l, m):
            a = m
            r = m-1
        else: l = m+1

    l, r = 0, n-1
    b = -1
    while l <= r:
        m = (l + r) // 2
        if query(1, m, r) != query(2, m, r):
            b = m
            l = m+1
        else: r = m-1

    print(f'! {a+1} {b+1}')


t = int(input())
for i in range(t): solve()