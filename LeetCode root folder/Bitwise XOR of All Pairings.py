# bit manipulation of xor:4
# ms
# Beats
# 60.47%
# you only need to know well about the characteristics of xor operation in order to solve this problem effortlessly.
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        res = 0
        if l2 % 2 == 1:
            for num in nums1:
                res ^= num
        if l1 % 2 == 1:
            for num in nums2:
                res ^= num
        return res