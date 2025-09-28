from collections import defaultdict, deque, Counter
from heapq import nlargest
from typing import List
from sortedcontainers import SortedList
import heapq, sys
from math import gcd, lcm, inf, sqrt
from functools import cache
sys.setrecursionlimit(1 << 20)




def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    res = 0
    for i in range(n):
        res += max(0, arr[i]-brr[i])
    print(res+1)

t = int(input())
for i in range(t):
    solve()

