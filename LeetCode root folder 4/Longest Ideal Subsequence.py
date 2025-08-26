# the 1000th leetcode question🎉🎉🎉🎉🥂🥂🎄: 5%
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0]*27 for _ in range(n)]
        def recursive(i, prev):
            nonlocal n
            if i >= n: return 0
            if dp[i][ord(prev)-ord('a')] != 0: return dp[i][ord(prev)-ord('a')]
            if prev == '{':
                a = recursive(i+1, prev)
                b = recursive(i+1, s[i]) + 1
            else:
                a = recursive(i+1, prev)
                if abs(ord(s[i])-ord(prev)) <= k: b = recursive(i+1, s[i]) + 1
                else: b = 0
            dp[i][ord(prev)-ord('a')] = max(a, b)
            return dp[i][ord(prev)-ord('a')]
        return recursive(0, '{')