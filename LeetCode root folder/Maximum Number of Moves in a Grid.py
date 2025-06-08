# brute force: tle
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # brute force
        row, col = len(grid), len(grid[0])
        def dfs(r, c, prev):
            if (
                r not in range(row) or
                c not in range(col) or
                grid[r][c] <= prev
            ):
                return 0
            cur = grid[r][c]
            return max(
                dfs(r, c+1, cur),
                dfs(r-1, c+1, cur),
                dfs(r+1, c+1, cur)
            ) + 1
        maxPath = 0
        for r in range(row):
            maxPath = max(maxPath, dfs(r, 0, -float('inf')))
        return maxPath-1

# dp solution:399
# ms
# Beats
# 10.15%
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # dp solution
        dp = {}
        row, col = len(grid), len(grid[0])
        def dfs(r, c, prev):
            if (r, c, prev) in dp:
                return dp[(r, c, prev)]
            if (
                r not in range(row) or
                c not in range(col) or
                grid[r][c] <= prev
            ):
                return 0
            cur = grid[r][c]
            res = max(
                dfs(r, c+1, cur),
                dfs(r-1, c+1, cur),
                dfs(r+1, c+1, cur)
            ) + 1
            dp[(r, c, prev)] = res
            return res
        maxPath = 0
        for r in range(row):
            maxPath = max(maxPath, dfs(r, 0, -float('inf')))
        return maxPath-1