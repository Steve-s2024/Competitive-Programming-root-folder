class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, 0
        total = 0
        while r < k:
            total += nums[r]
            r += 1
        maxVal = total
        while r < len(nums):
            total -= nums[l]
            total += nums[r]
            l += 1
            r += 1
            maxVal = max(maxVal, total)
        return maxVal / k