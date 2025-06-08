# holy, this is crazy, I didn't even expect to solve it, and I definitely gambled with this solution. it worked
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    offsetR, offsetC = 0, 0
    grid = [[0]*n for i in range(n)]
    cnt = n*n-1
    while cnt and offsetR < n//2:
        for c in range(offsetC, n-offsetC-1):
            grid[offsetR][c] = cnt
            # print(offsetR, c)
            cnt -= 1
        # print()
        for r in range(offsetR, n-offsetR-1):
            grid[r][n-offsetC-1] = cnt
            # print(r, n-offsetC-1)
            cnt -= 1
        # print()
        for c in range(n-offsetC-1, offsetR, -1):
            grid[n-offsetR-1][c] = cnt
            # print(n-offsetR-1, c)
            cnt -= 1
        # print()
        for r in range(n-offsetR-1, offsetC, -1):
            grid[r][offsetC] = cnt
            # print(r, offsetC)
            cnt -= 1
        # print()
        offsetR += 1
        offsetC += 1

    # print(grid)
    for row in grid:
        print(' '.join([str(e) for e in row]))

t = int(input())
for i in range(t):
    solve()


