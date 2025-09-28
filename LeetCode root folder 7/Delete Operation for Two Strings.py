# LCA solution: 18%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def recursive(i, j):
            nonlocal n, m
            if i >= n or j >= m: return 0
            if word1[i] == word2[j]: return recursive(i+1, j+1)+1
            return max(
                recursive(i+1, j),
                recursive(i, j+1)
            )
        mx = recursive(0, 0)
        return n-mx + m-mx