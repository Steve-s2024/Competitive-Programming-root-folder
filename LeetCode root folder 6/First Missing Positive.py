# follow the requirement, using linear time and 0 auxiliary space: 5%
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cur = nums[i] - 1
            while 0 <= cur < len(nums):
                a = nums[cur] - 1
                nums[cur] = inf
                cur = a

        for i in range(n):
            if nums[i] != inf: return i + 1
        return n + 1