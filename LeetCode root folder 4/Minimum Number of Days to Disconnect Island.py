# fixed the BFS and now it run in constant time: 1671ms 10%
class Solution:
    @staticmethod
    def spread(r, c, grid, vis):
        row, col = len(grid), len(grid[0])
        q = deque([(r, c)])
        vis.add((r, c))
        while q:
            r, c = q.popleft()
            for R, C in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if (
                    R in range(row) and
                    C in range(col) and
                    grid[R][C] == 1 and
                    (R, C) not in vis
                ):
                    vis.add((R, C))
                    q.append((R, C))

    def minDays(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        cnt = 0
        vis = set()
        for r in range(row):
            for c in range(col):
                if (r, c) not in vis and grid[r][c] == 1:
                    Solution.spread(r, c, grid, vis)
                    cnt += 1
        if cnt != 1:
            return 0

        for R in range(row):
            for C in range(col):
                if grid[R][C] == 1:
                    grid[R][C] = 0
                    cnt = 0
                    vis = set()
                    for r in range(row):
                        for c in range(col):
                            if (r, c) not in vis and grid[r][c] == 1:
                                Solution.spread(r, c, grid, vis)
                                cnt += 1
                    grid[R][C] = 1
                    if cnt != 1:
                        return 1

        return 2


# tle
class Solution:
    @staticmethod
    def spread(r, c, grid, vis):
        row, col = len(grid), len(grid[0])
        q = deque([(r, c)])
        while q:
            r, c = q.popleft()
            vis.add((r, c))
            for R, C in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if R in range(row) and C in range(col) and grid[R][C] == 1 and (R, C) not in vis:
                    q.append((R, C))

    def minDays(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        cnt = 0
        vis = set()
        for r in range(row):
            for c in range(col):
                if (r, c) not in vis and grid[r][c] == 1:
                    Solution.spread(r, c, grid, vis)
                    cnt += 1
        if cnt != 1:
            return 0

        for R in range(row):
            for C in range(col):
                if grid[R][C] == 1:
                    grid[R][C] = 0
                    cnt = 0
                    vis = set()
                    for r in range(row):
                        for c in range(col):
                            if (r, c) not in vis and grid[r][c] == 1:
                                Solution.spread(r, c, grid, vis)
                                cnt += 1
                    grid[R][C] = 1
                    if cnt != 1:
                        return 1

        return 2