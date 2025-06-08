# pretty good question, share similar pattern with
# the dp solution of last week's Q3, both using modulo
# dp: 78%
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1000000007
        row, col = len(grid), len(grid[0])
        dp = [[[0]*k for j in range(col)] for i in range(row)]
        dp[row-1][col-1][grid[row-1][col-1]%k] = 1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                val = grid[r][c]
                if r < row-1:
                    for i in range(k):
                        # i is the remain of modulo
                        dp[r][c][(i+val)%k] += dp[r+1][c][i] % MOD
                if c < col-1:
                    for i in range(k):
                        # i is the remain of modulo
                        dp[r][c][(i+val)%k] += dp[r][c+1][i] % MOD
        # for row in dp:
        #     print(row)
        return dp[0][0][0] % MOD