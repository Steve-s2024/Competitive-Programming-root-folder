# dp solution: tle
'''class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = {}

        def recursive(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]
            if remain == 0:
                return 0
            if remain < 0 or i >= len(nums):
                return -float('inf')

            maxLen = -float('inf')
            for j in range(i, len(nums)):
                maxLen = max(recursive(j + 1, remain - nums[j]), maxLen)
            maxLen += 1
            dp[(i, remain)] = maxLen
            return maxLen

        res = recursive(0, target)
        if res == -float('inf'):
            return -1
        else:
            return res'''

# dp solution no.2, optimized, not my idea:
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        for num in nums:
            if num > target:
                continue
            for i in range(len(dp) - num - 1, 0, -1):
                if dp[i] != -1:
                    dp[i + num] = max(dp[i] + 1, dp[i + num])
            dp[num] = max(1, dp[num])
            # print(num, dp)
        return dp[target]


