# brute-force
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute-force
        def dfs(tar, idx):
            if idx >= len(nums):
                if tar == 0:
                    return 1
                else:
                    return 0

            return (
                    dfs(tar - nums[idx], idx + 1) +
                    dfs(tar + nums[idx], idx + 1)
            )

        return dfs(target, 0)
'''


# dp solution:210
# ms
# Beats
# 16.48%
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp solution
        dp = {}

        def dfs(tar, idx):
            if (tar, idx) in dp:
                return dp[(tar, idx)]
            if idx >= len(nums):
                if tar == 0:
                    return 1
                else:
                    return 0

            dp[(tar, idx)] = (
                    dfs(tar - nums[idx], idx + 1) +
                    dfs(tar + nums[idx], idx + 1)
            )
            return dp[(tar, idx)]

        return dfs(target, 0)