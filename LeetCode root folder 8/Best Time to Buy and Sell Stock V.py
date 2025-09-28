# finally conquered this question, the one that ruined my weekly contest three month ago: 63%
# gotta keep practice bottom up DP, it's the hardest to write but most efficient, speed up the DP solution
# several folds than the recursive one.
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[-inf]*(k+1) for _ in range(3)]
        for i in range(k+1):
            dp[0][i] = 0
            dp[1][i] = prices[-1]
            dp[2][i] = -prices[-1]

        for i in range(n-2, -1, -1):
            tmp = [[-inf]*(k+1) for _ in range(3)]
            for j in range(k+1):
                if j: tmp[0][j] = max(dp[0][j], dp[1][j-1] - prices[i], dp[2][j-1] + prices[i])
                else: tmp[0][j] = dp[0][j]
                tmp[1][j] = max(dp[1][j], dp[0][j] + prices[i])
                tmp[2][j] = max(dp[2][j], dp[0][j] - prices[i])
            dp = tmp
        return dp[0][k]


# MLE on the second last testcase, a bottom up would fix it😀
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def recursive(i, f, c):
            nonlocal n
            if i >= n:
                if f == 0: return 0
                if f == 1: return prices[i - 1]
                if f == 2: return -prices[i - 1]

            res = recursive(i + 1, f, c)
            if f == 1:
                a = recursive(i + 1, 0, c - 1) + prices[i]
                res = max(res, a)
            if f == 2:
                a = recursive(i + 1, 0, c - 1) - prices[i]
                res = max(res, a)
            if f == 0 and c:
                a = recursive(i + 1, 1, c) - prices[i]
                b = recursive(i + 1, 2, c) + prices[i]
                res = max(res, a, b)
            return res

        return recursive(0, 0, k)


