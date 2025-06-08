# greedy solution with sorting:43
# ms
# Beats
# 32.96%
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        res = float('inf')
        for i in range(4):
            j = 4 - i
            res = min(nums[-j]-nums[i], res)
        return res