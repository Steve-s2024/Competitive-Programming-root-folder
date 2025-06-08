# greedy solution:55
# ms
# Beats
# 60.78%
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        total = 0
        for i in range(len(nums)):
            emptySpot = nums[i] - i - 1
            if emptySpot >= k:
                # print(nums[i], k)
                size = i + k  # size --> the size of the entire set of numbers 1,2,3...i+k, of which i of them already exist inside the input array (nums), and their sum is stored in 'total'.
                totalSum = (size) * (size + 1) // 2
                return totalSum - total
            total += nums[i]

        # since there are not enough empty spots for all k numbers in the range 1 to max(nums), we do the following
        size = len(nums) + k
        totalSum = (size) * (size + 1) // 2
        return totalSum - total




