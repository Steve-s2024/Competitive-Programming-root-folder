# longest palindromic subsequence type of DP over choices, rating of 1880 is an underestimation
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def fn(i, j, K):
            if i == j: return 1
            if i > j: return 0

            res = max(fn(i + 1, j, K), fn(i, j - 1, K))
            a, b = s[i], s[j]
            mi = min(abs(ord(a) - ord(b)), 26 - abs(ord(a) - ord(b)))
            if K >= mi: res = max(res, fn(i + 1, j - 1, K - mi) + 2)
            return res

        res = fn(0, n - 1, k)
        fn.cache_clear()
        return res
