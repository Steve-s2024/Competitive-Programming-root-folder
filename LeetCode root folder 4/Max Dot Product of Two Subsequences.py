# simple DP with additional negative handling: 37%
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if max(nums2) < 0 and min(nums1) > 0:
            return max(nums2) * min(nums1)
        n, m = len(nums1), len(nums2)
        @cache
        def recursive(i, j):
            if i >= n or j >= m:
                return 0
            a = recursive(i+1, j+1) + nums1[i]*nums2[j]
            b = recursive(i+1, j)
            c = recursive(i, j+1)
            return max(a, b, c)
        return recursive(0, 0)