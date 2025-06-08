# dp solution: 47%
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = {}
        def recursive(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]
            if i >= n and remain >= 0:
                return 0
            if remain <= 0:
                return -float('inf')

            res = 0
            total = 0
            size = 0
            for j in range(i, n):
                total += nums[j]
                size += 1
                res = max(res, recursive(j+1, remain-1) + total/size)
            dp[(i, remain)] = res
            return res
        return recursive(0, k)