# dp solution:154
# ms
# Beats
# 43.05%

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        maxSide = 0
        for r in range(len(matrix)):
            dp.append([])
            for c in range(len(matrix[0])):
                dp[r].append(0)
                if matrix[r][c] == '0':
                    continue

                n1 = dp[r][c - 1] if c > 0 else 0
                n2 = dp[r - 1][c] if r > 0 else 0
                # maxSide cannot exceed min(n1, n2) + 1
                side = min(n1, n2)
                # check the marginal one to determine if increase maxSide by one
                side += int(matrix[r - side][c - side])

                dp[r][c] = side
                maxSide = max(maxSide, side)

        # print(dp)
        return maxSide ** 2