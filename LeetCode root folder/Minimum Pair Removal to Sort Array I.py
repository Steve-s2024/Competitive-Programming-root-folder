# dumb as hell question, brute force
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def checkIncre(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        res = 0
        while checkIncre(nums) == False:
            # print(nums)
            sums = []
            for i in range(len(nums)-1):
                sums.append(nums[i]+nums[i+1])
                min_ = min(sums)
            for i in range(len(sums)):
                if sums[i] == min_:
                    # nums[i] + nums[i+1]
                    nums.pop(i)
                    nums[i] = sums[i]
                    break
            res += 1
        return res