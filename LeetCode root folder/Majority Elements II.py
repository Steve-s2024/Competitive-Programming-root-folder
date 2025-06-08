
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.append(nums[-1] + 1) # add the terminator for the last segment
        count = 1
        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                if count > (len(nums)-1) / 3.0:
                    res.append(nums[i])
                count = 1
        return res
