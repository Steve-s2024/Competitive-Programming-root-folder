class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        idx = len(nums) // 2
        median = nums[idx]
        if median == k:
            return 0
        elif median > k:
            i = idx
            while i >= 0:
                if nums[i] <= k:
                    break
                res += (nums[i] - k)
                i -= 1
        elif median < k:
            i = idx
            while i < len(nums):
                if nums[i] >= k:
                    break
                res += (k - nums[i])
                i += 1
        return res