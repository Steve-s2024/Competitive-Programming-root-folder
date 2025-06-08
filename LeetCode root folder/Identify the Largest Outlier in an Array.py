# simulation solution, with hash map:228
# ms
# Beats
# 67.83%
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        hashMap = Counter(nums)
        sum_ = sum(nums)
        res = -float('inf')
        for num in nums:
            # pretend num is the sum of all special numbers.
            curSum = sum_ - num # curSum --> num + outlier
            outlier = curSum - num
            if outlier in hashMap and (outlier != num or hashMap[outlier] > 1): # if outlier exists inside nums, update the res
                res = max(res, outlier)
        return res