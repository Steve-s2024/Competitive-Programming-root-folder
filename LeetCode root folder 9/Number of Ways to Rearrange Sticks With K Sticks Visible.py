# nailed it! 2333 rated problem solved independently under 30 minutes
# not even sure this will work at first

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        @cache
        def recursive(i, K):
            if i == 0: return 1 if K == 0 else 0
            res = recursive(i-1, K) * (n-i)
            if K: res += recursive(i-1, K-1)
            return res % mod
        res = recursive(n-1, k-1)
        recursive.cache_clear()
        return res
