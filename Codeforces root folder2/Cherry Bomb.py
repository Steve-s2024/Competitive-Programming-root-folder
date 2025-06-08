# not bad, moderate hard
from collections import defaultdict, deque
import heapq, math

def solve():
    [n, k] = [int(e) for e in input().split(' ')]
    arr = [int(e) for e in input().split(' ')]
    brr = [int(e) for e in input().split(' ')]

    target = float('inf')
    for i in range(n):
        if brr[i] != -1:
            target = arr[i] + brr[i]
            break
    if target != float('inf'):
        res = 0
        for i in range(n):
            if brr[i] != -1 and arr[i] + brr[i] != target:
                break
            if brr[i] == -1 and target - arr[i] not in range(k+1):
                break
        else:
            res = 1
        print(res)
    else:
        max_ = max(arr)
        min_ = min(arr)
        print(k - (max_-min_) + 1)

t = int(input())
for tt in range(t):
    solve()