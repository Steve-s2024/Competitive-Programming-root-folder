# go suck dic LC for MLE on my @cache solution and pass on this one with clearly 9 million iteration solution in worst
# case: 22%

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        arr = [0]*n
        for i in targetIndices: arr[i] = 1
        suf = [0]*n
        tot = 0
        for i in range(n-1, -1, -1):
            tot += arr[i]
            suf[i] = tot
        dp = [[None]*m for _ in range(n)]
        def recursive(i, j):
            if j >= m: return suf[i-1]-arr[i-1]
            if i >= n: return -inf
            if dp[i][j] != None: return dp[i][j]
            res = -inf
            if source[i] == pattern[j]: res = recursive(i+1, j+1)
            a = recursive(i+1, j) + arr[i]
            res = max(res, a)
            dp[i][j] = res
            return res
        return recursive(0, 0)
