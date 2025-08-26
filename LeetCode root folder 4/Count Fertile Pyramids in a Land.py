# pretty easy 2D DP question for this rating: 17%

class Solution:
    @staticmethod
    def getHeight(r, c, dp):
        row, col = len(dp), len(dp[0])
        if r + 1 >= row: return 0
        if c not in range(1, col - 1): return 0
        minHeight = float('inf')
        for i in range(c - 1, c + 2): minHeight = min(minHeight, dp[r + 1][i])
        return minHeight

    @staticmethod
    def getInverseHeight(r, c, dp):
        row, col = len(dp), len(dp[0])
        if r - 1 < 0: return 0
        if c not in range(1, col - 1): return 0
        minHeight = float('inf')
        for i in range(c - 1, c + 2): minHeight = min(minHeight, dp[r - 1][i])
        return minHeight

    def countPyramids(self, grid: List[List[int]]) -> int:
        dp = [ROW[:] for ROW in grid]
        res = 0
        row, col = len(grid), len(grid[0])
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if dp[r][c] == 1:
                    dp[r][c] = Solution.getHeight(r, c, dp) + 1
                    res += dp[r][c] - 1
        # print(dp)

        dp = [ROW[:] for ROW in grid]
        for r in range(row):
            for c in range(col):
                if dp[r][c] == 1:
                    dp[r][c] = Solution.getInverseHeight(r, c, dp) + 1
                    res += dp[r][c] - 1

        # print(dp)
        return res