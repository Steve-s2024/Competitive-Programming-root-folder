# the optimized code without the extra factor "n", converting to bottom up is always a torture, but this time it feels productive
# O(nk)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0]*(k+1)
        pre = [0]*(k+1)
        sm = 0
        for K in range(k+1):
            dp[K] = 1 if K <= n-1 else 0
            sm += dp[K]
            pre[K] = sm


        for i in range(n-1, 0, -1):
            dpTmp = [0]*(k+1)
            preTmp = [0]*(k+1)
            sm = 0
            for K in range(k+1):
                K_ = max(0, K-(i-1)) # with the current "i", can at most eliminate K to K_
                x = pre[K]-(pre[K_-1] if K_ else 0)
                dpTmp[K] = x % mod
                sm += dpTmp[K] % mod
                preTmp[K] = sm
            dp = dpTmp
            pre = preTmp

        return dp[k]



# TLE, will modify with summing up past result and get rid off the for j in range(1, i) part and replace with constant operation
#O(n^2k)
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        @cache
        def recursive(i, K):
            nonlocal mod
            if K < 0: return 0
            if i >= n: return 1 if K <= i-1 else 0
            res = recursive(i+1, K)
            for j in range(1, i):
                res += recursive(i+1, K-j)
                res %= mod
            return res
        return recursive(1, k)