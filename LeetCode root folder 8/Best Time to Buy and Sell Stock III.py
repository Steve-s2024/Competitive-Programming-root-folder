# crazy DP manipulation! best solution ever! state machine is about choosing the state of the current index
# in this case particularly, it can be open or close, it can have 2, 1 or 0 buys left. a total of 2*3 = 6 different states
# always, the state machine has a small number of states: 15%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recursive(i, f, c):
            if i >= n: return prices[i - 1] if f else 0
            res = recursive(i + 1, f, c)
            if f:
                a = recursive(i + 1, not f, c - 1) + prices[i]
                res = max(res, a)
            if not f and c:
                a = recursive(i + 1, not f, c) - prices[i]
                res = max(res, a)
            return res

        return recursive(0, 0, 2)
