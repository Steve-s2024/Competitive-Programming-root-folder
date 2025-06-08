# greedy solution:33
# ms
# Beats
# 51.92%
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            for i in range(len(nums1)):
                if nums1[i] != nums2[i]:
                    return -1
            return 0
        if sum(nums1) != sum(nums2):
            return -1
        diffs = []
        for i in range(len(nums1)):
            diff = abs(nums2[i]-nums1[i])
            if diff % k != 0:
                return -1
            diffs.append(diff)
        return sum(diffs) // k // 2