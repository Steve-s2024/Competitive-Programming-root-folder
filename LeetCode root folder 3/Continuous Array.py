# good question, prefix sum manipulation: 20%
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] != -1:
                idx = nums[i]-1
                while nums[idx] != -1:
                    nums[idx] = -1
                    idx = nums[idx]-1
                # now nums[idx] = -1
                res.append(idx)
        return res