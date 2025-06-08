# sliding window solution:15
# ms
# Beats
# 25.59%

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minLen = float('inf')
        total = 0
        while r < len(nums):
            while total < target:
                if r >= len(nums):
                    return minLen if minLen != float('inf') else 0
                total += nums[r]
                r += 1
            while total - nums[l] >= target:
                total -= nums[l]
                l += 1
            minLen = min(minLen, r - l)
            total -= nums[l]
            l += 1

        return minLen
