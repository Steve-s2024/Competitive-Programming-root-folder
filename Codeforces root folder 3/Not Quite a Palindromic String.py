#
from collections import defaultdict, deque, Counter
import heapq, math
import sys


def solve():
    n, k = [int(e) for e in input().split()]
    s = input()

    mp = Counter(s)
    a, b = mp['0'] if '0' in mp else 0, mp['1'] if '1' in mp else 0
    bad = n//2-k
    a-=bad
    b-=bad
    if a%2 == 0 and b%2 == 0 and min(a, b) >= 0:
        print('Yes')
    else:
        print('No')


t = int(input())
for i in range(t):
    solve()
