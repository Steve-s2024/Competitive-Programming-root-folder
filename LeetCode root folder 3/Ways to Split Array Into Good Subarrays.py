# 86%
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        MOD = 10**9 +7
        n = len(nums)
        res = 1
        cnt = 1
        flag = 0
        for i in range(n):
            if nums[i] == 1:
                if flag == 1:
                    res *= cnt
                    res %= MOD
                else:
                    flag = 1
                cnt = 1
            else:
                cnt += 1

        return res