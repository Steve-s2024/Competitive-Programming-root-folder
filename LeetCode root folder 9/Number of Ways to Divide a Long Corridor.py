# I probably mess up some subtle detail, otherwise the solution should not first MLE and then almost TLE

class Solution:
    def numberOfWays(self, cor: str) -> int:
        n = len(cor)
        mod = 10**9 + 7
        dp = [[-1]*3 for _ in range(n)]
        def recursive(i, x):
            nonlocal n, mod
            if i >= n: return 1 if x == 2 else 0
            if dp[i][x] != -1: return dp[i][x]
            x += 1 if cor[i] == 'S' else 0
            if x > 2: return 0
            res = (recursive(i+1, x) + (recursive(i+1, 0) if x == 2 else 0)) % mod
            dp[i][x] = res
            return res
        return recursive(0, 0)

