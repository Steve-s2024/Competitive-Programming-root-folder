# damn hard to observe the truth
from collections import defaultdict, deque, Counter
import heapq, math
import sys

def solve():
    n, m = [int(e) for e in input().split()]
    s = input()
    grid = []
    rowMp = defaultdict(int)
    colMp = defaultdict(int)
    for i in range(n):
        grid.append([int(e) for e in input().split()])
        for j in range(m):
            rowMp[i] += grid[i][j]
            colMp[j] += grid[i][j]
    s += '_' # add another placeholder
    r, c = 0, 0
    for char in s:
        a, b = rowMp[r], colMp[c]
        if char == 'D':
            grid[r][c] = -a
            rowMp[r] = 0
            colMp[c] += -a
            r += 1
        else:
            grid[r][c] = -b
            colMp[c] = 0
            rowMp[r] += -b
            c += 1

    # print(grid)
    for row in grid:
        print(' '.join([str(e) for e in row]))



t = int(input())
for i in range(t):
    solve()


