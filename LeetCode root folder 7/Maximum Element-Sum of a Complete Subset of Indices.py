# math-heavy question, you have to realize the trick of the greedy approach and how you should always choose
# the sequence i*1*1, i*2*2, i*3*3, i*4*4... where i belongs to {1, 2, 3, 4, 5, 6...}: 79%
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n+1):
            tot = 0
            j = 1
            while j*j*i-1 < n:
                tot += nums[j*j*i-1]
                j += 1
            res = max(res, tot)
        return res

