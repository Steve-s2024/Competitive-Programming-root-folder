class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = 1
        incre, decre = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                incre += 1
                decre = 1
            elif nums[i] > nums[i+1]:
                decre += 1
                incre = 1
            else:
                incre, decre = 1, 1
            maxLen = max(maxLen, incre, decre)
        return maxLen
