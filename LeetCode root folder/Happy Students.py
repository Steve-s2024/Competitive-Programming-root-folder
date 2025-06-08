# greedy solution:41
# ms
# Beats
# 78.30%
class Solution:
    def countWays(self, nums: List[int]) -> int:
        # greedy solution
        nums.sort()
        res = 0
        selected = 0
        for i in range(len(nums)):
            if (
                selected < nums[i] and
                (i == 0 or selected > nums[i-1])
            ):
                res += 1
            selected += 1
        if selected > nums[-1]:
            res += 1

        return res