# dynamic programming solution:71
# ms
# Beats
# 36.21%
# pretty interesting, and to finish it up the last part requires full attention.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for r in range(row)]
        for r in range(row):
            for c in range(col):
                side = 0
                if matrix[r][c] == 1:
                    side = 1
                    n1, n2 = 0, 0
                    if r > 0:
                        n1 = dp[r-1][c]
                    if c > 0:
                        n2 = dp[r][c-1]
                    extra = min(n1, n2)
                    if r-extra >= 0 and c-extra >= 0 and matrix[r-extra][c-extra] == 1:
                        side += extra
                    else:
                        side += max(extra-1, 0)
                dp[r][c] = side
                # print((r, c), side)
                res += side
        return res