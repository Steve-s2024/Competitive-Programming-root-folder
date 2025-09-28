# fking stupid leetcode fuck you and your serevr!!
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = 1
        MOD = 10 ** 9 + 7
        # coorDp, 0--> right, 1--> down
        coorDp = [[[(r, c), (r, c)] for c in range(col)] for r in range(row)]
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if grid[r][c] == 1:
                    if r + 1 < row and (coorDp[r + 1][c][1] != (r + 1, c) or grid[r + 1][c] == 0):
                        coorDp[r][c][0] = coorDp[r + 1][c][1]
                    if c + 1 < col and (coorDp[r][c + 1][0] != (r, c + 1) or grid[r][c + 1] == 0):
                        coorDp[r][c][1] = coorDp[r][c + 1][0]
        # print(coorDp)
        # for row in coorDp: print(row)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1: continue

                if r and grid[r - 1][c] == 0:
                    dp[r][c] += dp[r - 1][c]
                    dp[r][c] %= MOD
                if c and grid[r][c - 1] == 0:
                    dp[r][c] += dp[r][c - 1]
                    dp[r][c] %= MOD

                # print(dp[r][c], r, c)
                if r + 1 < row and c + 1 < col and grid[r + 1][c] == 1:
                    if coorDp[r + 1][c][1] != (r + 1, c):
                        R, C = coorDp[r + 1][c][1]
                        dp[R][C] += dp[r][c]
                        dp[R][C] %= MOD
                if r + 1 < row and c + 1 < col and grid[r][c + 1] == 1:
                    if coorDp[r][c + 1][0] != (r, c + 1):
                        R, C = coorDp[r][c + 1][0]
                        dp[R][C] += dp[r][c]
                        dp[R][C] %= MOD

        # print(dp)
        return dp[row - 1][col - 1]

