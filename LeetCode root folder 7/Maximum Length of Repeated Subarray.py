# don't know how, but the unusual knapsack solution work with one pass haha...: 5%
# this is clearly a way to find the longest continuous part of two array, which means
# you can actually use this to do string matching, it will only return the length though, which
# KMP can do better not to mention the time complexity difference.
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-1]*m for _ in range(n)]
        def recursive(i, j):
            if i >= n: return 0
            if j >= m: return 0
            if dp[i][j] != -1: return dp[i][j]
            recursive(i, j+1)
            recursive(i+1, j)
            dp[i][j] = 0
            if nums1[i] == nums2[j]:
                a = recursive(i+1, j+1)+1
                dp[i][j] = max(a, dp[i][j])
            return dp[i][j]
        recursive(0, 0)
        return max(e for row in dp for e in row)