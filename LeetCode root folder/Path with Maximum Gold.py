# garbage question, the same solution in c++ hit a tle everytime for no reason!:4980
# ms
# Beats
# 10.12%
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if (
                    (r not in range(row)) or
                    (c not in range(col)) or
                    (r, c) in visited or
                    grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))
            res = max(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            ) + grid[r][c]
            visited.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c))

        return res

