# today's contest feels easier than before, weired, but other
# performance is relatively bad.

import sys
import heapq, math
from collections import defaultdict, deque, Counter


def solve():
    n, k = [int(e) for e in input().split()]
    level = [int(e) for e in input().split()]
    gold = [int(e) for e in input().split()]

    idxMp = {}
    for i in range(n):
        idxMp[level[i]] = i

    pairs = []
    for i in range(n):
        pairs.append((level[i], gold[i]))

    pairs.sort(key = lambda i:i[0])
    res = [0]*n
    tot = 0
    minHeap = []
    for lev, gld in pairs:
        res[idxMp[lev]] = tot
        heapq.heappush(minHeap, gld)
        tot += gld
        if len(minHeap) > k:
            tot -= heapq.heappop(minHeap)


    print(' '.join(str(e) for e in res))






t = int(input())
for i in range(t):
    solve()