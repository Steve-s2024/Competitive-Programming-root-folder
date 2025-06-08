# brute force: TLE
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        res = 0
        for num in sorted(nums):
            for tar in numsDivide:
                if tar % num != 0:
                    break
            else:
                return res
            res += 1
        return -1