# simple dp solution: 5%

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[0] * m for i in range(n)]

        def recursive(i, j):
            nonlocal n, m
            if i >= n and j >= m:
                return True
            if i >= n:
                for k in range(j, m):
                    if p[k] != '*':
                        return False
                return True
            if j >= m:
                return False
            if dp[i][j] == 1:
                return False
            dp[i][j] = 1

            if s[i] == p[j] or p[j] == '?':
                if recursive(i + 1, j + 1):
                    return True
            elif p[j] == '*':
                for k in range(i, n + 1):
                    if recursive(k, j + 1):
                        return True
            return False

        return recursive(0, 0)