# neat problem, neat value squeezing solution. after all it is a greedy solution

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = len(nums)
        res = 0
        x = 0
        i = 0
        while x < n:
            while i < m and nums[i] <= x + 1:
                x += nums[i]
                i += 1
            if x >= n: break
            if i < n:  # missing something
                res += 1
                x += x + 1
        return res

