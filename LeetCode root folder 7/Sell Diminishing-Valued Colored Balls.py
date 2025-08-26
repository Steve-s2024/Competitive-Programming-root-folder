# basic binary search question: 5%
# couldn't figure out the optimized version though.
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        n = len(inventory)
        l, r = 0, max(inventory)
        res = 0
        while l <= r:
            m = (l+r)//2
            k = orders
            tot = 0
            cnt = 0
            for i in range(n):
                a = inventory[i]
                if a >= m: cnt += 1
                tot += max(a*(a+1)//2 - m*(m+1)//2, 0)
                k -= max(a-m, 0)
            if k >= 0:
                tot += min(k, cnt) * m
                res = max(res, tot)
                r = m-1
            else: l = m+1
        return res % MOD

