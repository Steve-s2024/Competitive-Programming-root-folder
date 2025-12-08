# nice question, i thought I can one greedy solve it, but turn out the intricate logic of the problem require
# simulation of my greedy idea, which still only take O(n) time
from collections import defaultdict, deque, Counter
from math import inf, ceil, floor, sqrt, gcd, lcm
import heapq, math
import sys

sys.setrecursionlimit(100000000)



def solve():
    n, m, k = [int(e) for e in input().split()]
    arr = [0]*n
    psize = 0
    res = 0
    for p in range(1, n+1):
        numOfP = floor(n/p)
        re = n%p
        a = ceil(k/p)
        if numOfP > m*a:
            if p > res:
                res = p
                psize = p
        elif numOfP == m*a:
            if re > res:
                res = re
                psize = p

    for i in range(0, n, psize):
        for j in range(min(psize, n-i)):
            arr[i+j] = j

    print(' '.join(str(e) for e in arr))


t = int(input())
for i in range(t):
    solve()