# tle on testcase 59
def solve():
    row, col, n, p = [int(e) for e in input().split()]
    grid = []
    for i in range(row):
        grid.append([int(e) for e in input().split()])

    coor = None
    for r in range(row):
        for c in range(col):
            if grid[r][c] == p:
                coor = (r, c)
                break
        else:
            continue
        break

    hashSet = set()
    while True:
        r, c = coor
        val = grid[r][c]
        nextCoor = None
        for R, C in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
            if (
                R in range(row) and
                C in range(col) and
                grid[R][C] != 0
            ):
                val2 = grid[R][C]
                diff = val2 - val
                if p+diff in range(1, n+1):
                    hashSet.add(p+diff)
                if val2 == val-1:
                    nextCoor = (R, C)
        coor = nextCoor
        if val == 1:
            break
    print(str(len(hashSet))+'/'+str(n-1))
solve()

