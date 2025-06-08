# somewhat intuitive dp solution, not the typical dp, it is finding
# element from small to large and incorporate dp: 15%
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[1] * col for _ in range(row)]

        arr = []
        for r in range(row):
            for c in range(col):
                arr.append((grid[r][c], r, c))

        arr.sort(key=lambda i: i[0])
        for val, r, c in arr:
            for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                        R in range(row) and
                        C in range(col) and
                        grid[R][C] < val
                ):
                    dp[r][c] += dp[R][C]
                    dp[r][c] %= 10 ** 9 + 7

        # print(dp)
        res = 0
        for r in range(row):
            for c in range(col):
                res += dp[r][c]
                res %= 10 ** 9 + 7
        return res
