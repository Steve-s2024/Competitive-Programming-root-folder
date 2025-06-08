# dfs solution O(m*n):327
# ms
# Beats
# 5.34%
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal count, valid
            if (
                    r not in range(row) or
                    c not in range(col)
            ):
                valid = True
                return
            if grid[r][c] in [0, 2]:
                return
            count += 1
            grid[r][c] = 2
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 2:
                    count = 0
                    valid = False
                    dfs(r, c)
                    if valid == False:
                        res += count
        return res

