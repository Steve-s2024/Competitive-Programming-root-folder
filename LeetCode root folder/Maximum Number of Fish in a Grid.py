# dfs & hash set solution: 108ms

'''class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxCount = 0
        visited = set()
        count = 0

        def dfs(r, c):
            nonlocal count
            if (
                    r not in range(row) or
                    c not in range(col) or
                    (r, c) in visited or
                    grid[r][c] == 0
            ):
                return
            visited.add((r, c))

            count += grid[r][c]
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                count = 0
                dfs(r, c)
                maxCount = max(maxCount, count)
        return maxCount'''


