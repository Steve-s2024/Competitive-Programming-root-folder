

# depricated
from collections import defaultdict, deque
import heapq, math

t = int(input())
for tt in range(t):
    [n, m, k] = [int(e) for e in input().split(' ')]
    arr = [['0'] * m for i in range(n)]
    q = deque([(0, 0, 1)])
    visited = set()
    hashMap = {}
    for i in range(1, k+1):
        hashMap[i] = n*m // k

    for r in range(n):
        for c in range(m):
            for key in hashMap:
                if (
                    (r == 0 or str(key) != arr[r-1][c]) and
                    (c == 0 or str(key) != arr[r][c-1])
                ):
                    arr[r][c] = str(key)
                    hashMap[key]-=1
                    if hashMap[key] == 0:
                        del hashMap[key]
                    break
    # print(arr)
    for row in arr:
        print(' '.join(row))