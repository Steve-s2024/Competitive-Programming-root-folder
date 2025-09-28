# pretty easy, did all the Best Time to Buy and Sell Stock series. used this as a bottom up DP practice: 53%
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0, prices[-1]-fee]
        for i in range(n-2, -1, -1):
            tmp = [0, 0]
            tmp[0] = max(dp[0], dp[1]-prices[i])
            tmp[1] = max(dp[1], dp[0]+prices[i]-fee)
            dp = tmp
        return dp[0]