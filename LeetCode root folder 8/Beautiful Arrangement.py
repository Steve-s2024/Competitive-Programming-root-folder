# didn't expect it to run so fast...: 94%
class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def recursive(i, mask):
            nonlocal n
            if i > n: return 1
            res = 0
            for j in range(1, n + 1):
                if mask & (1 << j): continue
                if i % j == 0 or j % i == 0: res += recursive(i + 1, mask | (1 << j))
            return res

        return recursive(1, 0)


# and also super weird why the bottom up DP is much slower: 13%
class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [0]*(1<<n)
        dp[-1] = 1
        for i in range(n-1, -1, -1):
            tmp = [0]*(1<<n)
            for j in range((1<<n)):
                for k in range(n):
                    if j&(1<<k): continue
                    if ((i+1)%(k+1)) * ((k+1)%(i+1)) == 0: tmp[j] += dp[j|(1<<k)]
            dp = tmp
        return dp[0]
