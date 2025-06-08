# dp solution, but dp is not optimal? : 24%
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = {}
        MOD = 1000000007
        def recursive(day):
            if day in dp:
                return dp[day]
            res = 1
            for j in range(day+delay, min(n+1, day+forget)):
                res += recursive(j)
            if day + forget <= n:
                res -= 1
            dp[day] = res
            return res % MOD
        return recursive(1) % MOD