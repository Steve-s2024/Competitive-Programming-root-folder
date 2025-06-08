# can't believe how easy this is as a 1200 rated question
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    n, m = [int(e) for e in input().split()]
    pairs = []
    for i in range(n):
        arr = [int(e) for e in input().split()]
        pairs.append((arr, sum(arr)))
    pairs.sort(key = lambda i : i[1], reverse = True)
    res = 0
    total = 0
    for i in range(n):
        for j in range(m):
            total += pairs[i][0][j]
            res += total
    print(res)





t = int(input())
for tt in range(t):
    solve()