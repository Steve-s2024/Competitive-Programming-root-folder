# credit for editorial, the most optimal
def bfs(r, c, grid):
    row, col = len(grid), len(grid[0])
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        if r in range(row) and c in range(col):
            grid[r][c] = '_'

        for R, C, dir in [(r + 1, c, 'U'), (r - 1, c, 'D'), (r, c + 1, 'L'), (r, c - 1, 'R')]:
            if R in range(row) and C in range(col) and grid[R][C] == dir:
                q.append((R, C))

def solve():
    n, m = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        s = input()
        grid.append(list(s))
    row, col = n, m

    for r in range(row):
        bfs(r, -1, grid)
        bfs(r, col, grid)
    for c in range(col):
        bfs(-1, c, grid)
        bfs(row, c, grid)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '?':
                grid[r][c] = '_'
                for R, C, dir in [(r + 1, c, 'U'), (r - 1, c, 'D'), (r, c + 1, 'L'), (r, c - 1, 'R')]:
                    if R in range(row) and C in range(col) and grid[R][C] != '_':
                        grid[r][c] = '?'
                        break

    res = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] != '_':
                res += 1

    print(res)

t = int(input())
for i in range(t):
    solve()


# optimized solution for only finding the bad cells, TLE
from collections import defaultdict, deque, Counter
import heapq, math
import sys

def bfs(r, c, grid, visited):
    row, col =len(grid), len(grid[0])
    q = deque([(r, c)])
    cnt = 0
    while q:
        r, c = q.popleft()
        grid[r][c] = '!' # mark as visited
        visited[(r, c)] = 2
        cnt += 1
        for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if R in range(row) and C in range(col) and grid[R][C] == '?':
                q.append((R, C))
    if cnt == 1:
        flag = False
        for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (R, C) in visited and visited[(R, C)] == 2:
                flag = True
        visited[(r, c)] = 2 if flag else 1


def dfs(r, c, grid, visited):
    flag = False # false --> no cycle, true --> cycle
    row, col = len(grid), len(grid[0])
    path = set([(r, c)])
    while True:
        for R, C, dir in [(r + 1, c, 'D'), (r - 1, c, 'U'), (r, c + 1, 'R'), (r, c - 1, 'L')]:
            if grid[r][c] == dir:
                r, c = R, C
                break

        if r not in range(row) or c not in range(col):
            break
        if grid[r][c] == '?':
            visited[(r, c)] = 2 # mark the ? spot temporarily
            flag = True
            break
        if (r, c) in path:
            flag = True
            break

        path.add((r, c))

    for r, c in path:
        visited[(r, c)] = 2 if flag else 1




def solve():
    n, m = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        s = input()
        grid.append(list(s))
    row, col = n, m
    visited = {}
    res = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] != '?' and (r, c) not in visited:
                dfs(r, c, grid, visited)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '?' and (r, c) not in visited:
                bfs(r, c, grid, visited)

    for val in visited.values():
        if val == 2:
            res += 1

    # print(grid)
    print(res)

t = int(input())
for i in range(t):
    solve()




# TLE long ass as hell
def bfs(r, c, grid):
    row, col = len(grid), len(grid[0])
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for R, C, dir in [(r+1, c, 'U'), (r-1, c, 'D'), (r, c+1, 'L'), (r, c-1, 'R')]:
            if (
                R in range(row) and
                C in range(col) and
                grid[R][C] == '?'
            ):
                grid[R][C] = dir
                q.append((R, C))

def dfs(rSrc, cSrc, grid, visited):
    row, col = len(grid), len(grid[0])
    for rSrt, cSrt in [(rSrc+1, cSrc), (rSrc-1, cSrc), (rSrc, cSrc+1), (rSrc, cSrc-1)]:
        r, c = rSrt, cSrt
        if r not in range(row) or c not in range(col):
            continue
        path = [(r, c)]
        vis = set()
        vis.add((r, c))
        while True:
            for R, C, dir in [(r+1, c, 'D'), (r-1, c, 'U'), (r, c+1, 'R'), (r, c-1, 'L')]:
                if grid[r][c] == dir:
                    r, c = R, C
                    break

            if (r, c) in visited:
                for rr, cc in path:
                    visited[(rr, cc)] = visited[(r, c)] # either 1 or 2
                break
            elif r not in range(row) or c not in range(col):
                for rr, cc in path:
                    visited[(rr, cc)] = 1 # 1 --> escapable
                break
            elif (r, c) in vis:
                for rr, cc in path:
                    visited[(rr, cc)] = 2 # 2 --> non-escapable
                break
            elif grid[r][c] == '?':
                for rr, cc, dir in [(r+1, c, 'D'), (r-1, c, 'U'), (r, c+1, 'R'), (r, c-1, 'L')]:
                    if (rr, cc) == path[-1]:
                        grid[r][c] = dir

            vis.add((r, c))
            path.append((r, c))

    grid[rSrc][cSrc] = 'U'
    visited[(rSrc, cSrc)] = 1
    for R, C, dir in [(rSrc+1, cSrc, 'D'), (rSrc-1, cSrc, 'U'), (rSrc, cSrc+1, 'R'), (rSrc, cSrc-1, 'L')]:
        if R not in range(row) or C not in range(col):
            continue
        if visited[(R, C)] == 2:
            grid[rSrc][cSrc] = dir
            visited[(rSrc, cSrc)] = 2
            break


def find(r, c, grid, visited):
    row, col = len(grid), len(grid[0])
    path = [(r, c)]
    vis = set()
    vis.add((r, c))
    while True:
        for R, C, dir in [(r + 1, c, 'D'), (r - 1, c, 'U'), (r, c + 1, 'R'), (r, c - 1, 'L')]:
            if grid[r][c] == dir:
                r, c = R, C
                break

        if (r, c) in visited:
            for rr, cc in path:
                visited[(rr, cc)] = visited[(r, c)]  # either 1 or 2
            break
        elif r not in range(row) or c not in range(col):
            for rr, cc in path:
                visited[(rr, cc)] = 1  # 1 --> escapable
            break
        elif (r, c) in vis:
            for rr, cc in path:
                visited[(rr, cc)] = 2  # 2 --> non-escapable
            break

        vis.add((r, c))
        path.append((r, c))


def solve():
    n, m = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        s = input()
        grid.append(list(s))

    for r in range(n):
        for c in range(m):
            if grid[r][c] == '?':
                bfs(r, c, grid)

    # print(grid)

    visited = {}
    for r in range(n):
        for c in range(m):
            if (r, c) not in visited and grid[r][c] == '?':
                dfs(r, c, grid, visited)

    # print(grid)

    for r in range(n):
        for c in range(m):
            if (r, c) not in visited:
                find(r, c, grid, visited)

    res = 0
    for val in visited.values():
        if val == 2:
            res += 1
    print(res)


t = int(input())
for i in range(t):
    solve()


# the algorithm to find the actual labyrinth, I thought this is what needed...
from collections import defaultdict, deque, Counter


def bfs(r, c, grid):
    row, col = len(grid), len(grid[0])
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for R, C, dir in [(r + 1, c, 'U'), (r - 1, c, 'D'), (r, c + 1, 'L'), (r, c - 1, 'R')]:
            if (
                    R in range(row) and
                    C in range(col) and
                    grid[R][C] == '?'
            ):
                grid[R][C] = dir
                q.append((R, C))


def dfs(rSrc, cSrc, grid, visited):
    row, col = len(grid), len(grid[0])
    for rSrt, cSrt in [(rSrc + 1, cSrc), (rSrc - 1, cSrc), (rSrc, cSrc + 1), (rSrc, cSrc - 1)]:
        r, c = rSrt, cSrt
        if r not in range(row) or c not in range(col):
            continue
        path = [(r, c)]
        vis = set()
        vis.add((r, c))
        while True:
            for R, C, dir in [(r + 1, c, 'D'), (r - 1, c, 'U'), (r, c + 1, 'R'), (r, c - 1, 'L')]:
                if grid[r][c] == dir:
                    r, c = R, C
                    break

            if (r, c) in visited:
                for rr, cc in path:
                    visited[(rr, cc)] = visited[(r, c)]  # either 1 or 2
                break
            elif r not in range(row) or c not in range(col):
                for rr, cc in path:
                    visited[(rr, cc)] = 1  # 1 --> escapable
                break
            elif (r, c) in vis:
                for rr, cc in path:
                    visited[(rr, cc)] = 2  # 2 --> non-escapable
                break
            elif grid[r][c] == '?':
                for rr, cc, dir in [(r + 1, c, 'D'), (r - 1, c, 'U'), (r, c + 1, 'R'), (r, c - 1, 'L')]:
                    if (rr, cc) == path[-1]:
                        grid[r][c] = dir

            vis.add((r, c))
            path.append((r, c))

    grid[rSrc][cSrc] = 'U'
    visited[(rSrc, cSrc)] = 1
    for R, C, dir in [(rSrc + 1, cSrc, 'D'), (rSrc - 1, cSrc, 'U'), (rSrc, cSrc + 1, 'R'), (rSrc, cSrc - 1, 'L')]:
        if R not in range(row) or C not in range(col):
            continue
        if visited[(R, C)] == 2:
            grid[rSrc][cSrc] = dir
            visited[(rSrc, cSrc)] = 2
            break


def solve():
    n, m = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        s = input()
        grid.append(list(s))

    for r in range(n):
        for c in range(m):
            if grid[r][c] == '?':
                bfs(r, c, grid)

    # print(grid)

    visited = {}
    for r in range(n):
        for c in range(m):
            if (r, c) not in visited and grid[r][c] == '?':
                dfs(r, c, grid, visited)

    # print(grid)

    for row in grid:
        print(' '.join([str(e) for e in row]))


t = int(input())
for i in range(t):
    solve()
