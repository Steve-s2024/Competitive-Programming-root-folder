# almost exactly the same as best time to buy and sell stock III: 19%
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recursive(i, f, c):
            nonlocal n
            if i >= n: return prices[i - 1] if f else 0
            res = recursive(i + 1, f, c)
            if f:
                a = recursive(i + 1, not f, c - 1) + prices[i]
                res = max(res, a)
            if not f and c:
                a = recursive(i + 1, not f, c) - prices[i]
                res = max(res, a)
            return res

        return recursive(0, 0, k)