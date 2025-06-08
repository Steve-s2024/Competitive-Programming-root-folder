# good work, hard question, dp, and two robot --> two variable
# build on standard bottom up dp but with two pointers to pick from
# so the state is about two index: 40%
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for i in range(col)]
        for i in range(col):
            for j in range(i+1, col):
                dp[i][j] = grid[row-1][i] + grid[row-1][j]

        def findMax(I, J):
            res = 0
            for i in range(I-1, I+2):
                if i in range(col):
                    for j in range(J-1, J+2):
                        if j in range(col):
                            if i != j:
                                res = max(res, dp[i][j])
            return res

        for r in range(row-2, -1, -1):
            tmp = [[0] * col for i in range(col)]
            for i in range(col):
                for j in range(i+1, col):
                    val1, val2 = grid[r][i], grid[r][j]
                    tmp[i][j] = findMax(i, j) + val1+val2
            dp = tmp
        
        # print(dp)
        return dp[0][col-1]