class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if count == 0:
                    return False
                count -= 1
        return nums[0] >= nums[-1] if count == 0 else True