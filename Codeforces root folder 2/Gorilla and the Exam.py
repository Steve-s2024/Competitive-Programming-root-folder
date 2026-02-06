# too slow
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    mp = Counter(nums)
    vals = list(mp.values())
    vals.sort()
    total = 0
    i = 0
    m = len(vals)
    while i < m and total + vals[i] <= k:
        total += vals[i]
        i+=1
    print(max(m-i, 1))


t = int(input())
for tt in range(t):
    solve()