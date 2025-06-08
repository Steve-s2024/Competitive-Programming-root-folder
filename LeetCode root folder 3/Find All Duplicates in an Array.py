# wasted a lot of time on figuring out the way to use input
# array as the hashmap while not modify it so the data is contaminated
# this way I can use the array to track duplicate while not corrupt
# the data inside the array: 41%
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            tmp = abs(nums[i])
            idx = tmp-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                res.append(abs(nums[i]))
        return res