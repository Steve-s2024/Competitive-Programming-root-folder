
# don't know why it's so slow: MLE
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        a = word1 + word2
        n = len(a)
        dp = [[[[-1]*2 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        def recursive(i, j, f1, f2):
            if dp[i][j][f1][f2] != -1: return dp[i][j][f1][f2]
            if i == j: return 1 if f1 and f2 else -inf
            if i > j: return 0 if f1 and f2 else -inf
            if a[i] == a[j]:
                if i in range(len(word1)): f1 = 1
                if j in range(len(word1), n): f2 = 1
                res = recursive(i+1, j-1, f1, f2) + 2
            else:
                res = max(
                    recursive(i+1, j, f1, f2),
                    recursive(i, j-1, f1, f2)
                )
            dp[i][j][f1][f2] = res
            return res
        res = recursive(0, n-1, 0, 0)
        return res if res != -inf else 0
