

# depricated
import heapq, math
from collections import defaultdict, deque

def getSum(r, k, grid):
    res = 0
    for val in grid[r]:
        res += min(val, k)
    return res
            
def solve():
    n = int(input())
    grid = []
    max_ = 0
    for i in range(n):
        grid.append([int(e) for e in input().strip().split(' ')])
        max_ = max(max_, max(grid[i]))
    # print(grid)
    # since two factor to consider, way not nested binary search
    minOp = max_
    l, r = 1, max_
    while l <= r:
        m = (l+r) // 2
        # simulate with m as 'k'
        target = getSum(0, m, grid)
            
        score = 0
        for r in range(1, n):
            if target < getSum(r, m, grid):
                score += 1
        
        # binary search the min op for when score == 'score'
        minOp = m
        L, R = 1, m
        while L <= R:
            M = (L + R) // 2
            TARGET = getSum(0, M, grid)
            SCORE = 0
            for r in range(1, n):
                if TARGET < getSum(r, M, grid):
                    SCORE += 1
            if SCORE >= score:
                minOp = M
                R = M-1
            elif SCORE < score:
                L = M+1
        
        l = m+1
    print(minOp)
        

t = int(input())
for tt in range(t):
    solve()