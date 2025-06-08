# brute-force solution:
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        profits = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        maxProfit = 0
        def dfs(idx, prev, profit):
            nonlocal maxProfit
            if idx >= len(profits):
                maxProfit = max(maxProfit, profit)
                return

            dfs(idx+1, prev, profit)
            if prev == idx-1 or prev < idx - 2:
                dfs(idx+1, idx, profit + profits[idx])
        dfs(0, -3, 0)
        return maxProfit
'''

# dp solution, time complexity passed, now optimize the space complexity: memory limit exceeded
'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp solution
        profits = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        dp = {}

        def dfs(idx, sell):
            if idx >= len(profits):
                return 0

            if (idx, sell) in dp:
                return dp[(idx, sell)]

            if sell == idx - 1 or sell < idx - 2:
                a = dfs(idx + 1, sell)
                b = dfs(idx + 1, idx) + profits[idx]
            else:
                a = dfs(idx + 1, sell)
                b = 0

            dp[(idx, sell)] = max(a, b)
            return dp[(idx, sell)]
        res = dfs(0, -3)
        return res'''


# dp solution, space complexity handled:19
# ms
# Beats
# 8.72%
# this is the entry of 2D dp world for me
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp solution
        profits = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        dp = {}

        def dfs(idx, sell):
            if idx >= len(profits):
                return 0

            if (idx, max(sell, idx - 3)) in dp:
                return dp[(idx, max(sell, idx - 3))]

            if sell == idx - 1 or sell < idx - 2:
                a = dfs(idx + 1, sell)
                b = dfs(idx + 1, idx) + profits[idx]
            else:
                a = dfs(idx + 1, sell)
                b = 0

            dp[(idx, max(sell, idx - 3))] = max(a, b)
            return dp[(idx, max(sell, idx - 3))]

        res = dfs(0, -3)
        return res