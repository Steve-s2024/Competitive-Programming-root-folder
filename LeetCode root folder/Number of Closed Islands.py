# dfs solution:43
# ms
# Beats
# 6.77%
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            nonlocal row, col, increment
            if r in [0, row - 1] or c in [0, col - 1]:
                increment = 0

            visited.add((r, c))
            step = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
            for R, C in step:
                if (
                        R in range(row) and
                        C in range(col) and
                        (R, C) not in visited and
                        grid[R][C] != 1
                ):
                    dfs(R, C)
            return res

        res = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] != 1:
                    # print(r, c)
                    increment = 1
                    dfs(r, c)
                    res += increment
        return res


