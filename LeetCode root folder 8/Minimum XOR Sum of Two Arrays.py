# three minutes to finish this 2100 rated question, though I know at the start that this is a bitmask DP question: 41%
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def recursive(i, mask):
            if i >= n: return 0
            res = inf
            for j in range(m):
                if (1<<j) & mask: continue
                res = min(res, recursive(i+1, mask|(1<<j)) + (nums1[i]^nums2[j]))
            return res
        return recursive(0, 0)