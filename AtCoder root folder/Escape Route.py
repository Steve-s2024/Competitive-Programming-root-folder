# multi-source bfs, almost TLE
def solve():
    h, w = [int(e) for e in input().split()]
    grid = []
    for i in range(h):
        grid.append(list(input()))

    # multi-source bfs spread, like in rotten orange
    q = deque([])
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'E':
                q.append((r, c))

    ref = ['^', 'v', '<', '>']
    while q:
        r, c = q.popleft()
        for idx, coor in enumerate([(r+1, c),(r-1, c),(r, c+1),(r, c-1)]):
            R, C = coor
            if (
                R in range(h) and C in range(w) and
                grid[R][C] == '.'
            ):
                grid[R][C] = ref[idx]
                q.append((R, C))
    # print(grid)
    for row in grid:
        print(''.join(row))

solve()