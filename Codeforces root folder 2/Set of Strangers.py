# the idea is correct, maybe it will not hit TLE with c++
# c++ worked like a charm, beat the hell out of python
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    [n, m] = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        row = [int(e) for e in input().split()]
        grid.append(row)
    
    hashMap = {}
    for r in range(n):
        for c in range(m):
            val = grid[r][c]
            if val not in hashMap:
                hashMap[val] = 1
            elif hashMap[val] == 1:
                for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if (
                        R in range(n) and
                        C in range(m) and
                        grid[R][C] == val
                    ):
                        hashMap[val] = 2


    res = sum(hashMap.values()) - max(hashMap.values())
    print(res)



t = int(input())
for tt in range(t):
    solve()