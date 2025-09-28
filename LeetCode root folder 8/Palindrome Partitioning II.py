# interesting n^2 way of searching for all sub palindromes, and incorporate with knapsack. a good way to save time
# is to study the state transformation and replace recursive call with a bottom up DP: 20%
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[] for _ in range(n)]
        mp = [[] for _ in range(n)]
        for i in range(n):
            dp[0].append((i, i))
            mp[i].append(i)

        for i in range(1, n):
            if s[i - 1] == s[i]:
                dp[1].append((i - 1, i))
                mp[i - 1].append(i)

        for i in range(2, n):
            for l, r in dp[i - 2]:
                if l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                    dp[i].append((l - 1, r + 1))
                    mp[l - 1].append(r + 1)

        @cache
        def recursive(i):
            if i >= n: return 0
            res = inf
            for j in mp[i]:
                a = recursive(j + 1) + 1
                res = min(res, a)
            return res

        return recursive(0) - 1
