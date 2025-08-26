# why can't I just see such a simple solution!!! have to look at the longest common subsequence solution
# to realize that: 73%

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def recursive(i, j):
            if i == j: return 1
            if i > j: return 0

            if s[i] == s[j]: return recursive(i+1, j-1)+2
            else:
                return max(
                    recursive(i+1, j),
                    recursive(i, j-1)
                )
        return recursive(0, n-1)