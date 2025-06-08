# turns out its just brute force... I knew it cause of
# the constraint and the impossible nature of the problem
# to solve without brute-force.
# I didn't choose the brute force util a while into the problem.
# that is because it's hard to analyze the time complexity, and by
# approximating it as a subsequence enumeration process, the time
# will guarantee TLE, only because of the Domino which makes this
# brute force viable
def solve():
    h, w = [int(e) for e in input().split()]
    grid = []
    for i in range(h):
        grid.append([int(e) for e in input().split()])

    vis = set()
    def recursive(r, c, tot):
        nonlocal h, w
        if r >= h:
            return tot
        if c < w-1:
            R, C = r, c+1
        else:
            R, C = r+1, 0

        res = 0
        if (r, c) in vis:
            res = max(res, recursive(R, C, tot))
        else:
            res = max(res, recursive(R, C, tot^grid[r][c]))
            if c < w-1 and (r, c+1) not in vis:
                vis.add((r, c+1))
                res = max(res, recursive(R, C, tot))
                vis.remove((r, c+1))
            if r < h-1 and (r+1, c) not in vis:
                vis.add((r+1, c))
                res = max(res, recursive(R, C, tot))
                vis.remove((r+1, c))
        return res
    print(recursive(0, 0, 0))

solve()



# why not working??
def solve():
    h, w = [int(e) for e in input().split()]
    grid = []
    for i in range(h):
        grid.append([int(e) for e in input().split()])

    vis = set()

    def recursive(r, c):
        nonlocal h, w
        if r > h - 1:
            return 0

        if c >= w - 1:
            R, C = r + 1, 0
        else:
            R, C = r, c + 1

        res = -1
        if (r, c) not in vis:
            res = max(res, recursive(R, C) ^ grid[r][c])
            if c < w - 1 and (r, c + 1) not in vis:
                vis.add((r, c + 1))
                res = max(res, recursive(R, C))
                vis.remove((r, c + 1))
            if r < h - 1 and (r + 1, c) not in vis:
                vis.add((r + 1, c))
                res = max(res, recursive(R, C))
                vis.remove((r + 1, c))
        else:
            res = recursive(R, C)
        return res

    print(recursive(0, 0))


solve()



# deprecated
def solve():
    h, w = [int(e) for e in input().split()]
    grid = []
    line = []
    for i in range(h):
        grid.append([int(e) for e in input().split()])
        line.extend(grid[-1])
    def backtrack(i):
        nonlocal h, w
        if i >=h*w:
            return 0
        return max(
            backtrack(i+1),
            backtrack(i+1)^line[i]
        )
    print(backtrack(0))



solve()