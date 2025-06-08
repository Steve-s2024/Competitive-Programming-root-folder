# this does not deserve to be rated this high... it is much
# easier then the LIS question below it: 95%
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        total = 0
        for i in range(k):
            total += nums[i]
        dp[k-1] = total

        for i in range(k, n):
            total += nums[i]
            total -= nums[i-k]
            dp[i] = max(dp[i-k], 0)
            dp[i] += total
        # print(dp)
        return max(dp[k-1:])
