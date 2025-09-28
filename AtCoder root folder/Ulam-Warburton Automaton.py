# this is a grid pattern with a lot of property discovered by others, which can be found on wikipedia. in the end
# this problem is just brute force simulate with multi-source bfs
from collections import defaultdict, deque, Counter



def solve():
    h, w = [int(e) for e in input().split()]
    grid = []
    for i in range(h):
        arr = list(input())
        grid.append(arr)

    vis = set()
    q = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                q.append((i, j))
                vis.add((i, j))

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if i in range(h) and j in range(w) and (i, j) not in vis:
                    sm = 0
                    for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if r in range(h) and c in range(w) and grid[r][c] == '#': sm += 1
                    if sm == 1:
                        vis.add((i, j))
                        q.append((i, j))
        for i, j in q:
            grid[i][j] = '#'


    # for r in grid: print(r)
    res = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#': res += 1
    print(res)







solve()
