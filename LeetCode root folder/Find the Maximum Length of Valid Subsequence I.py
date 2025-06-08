# greedy solution: 50%
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 1
        for i in range(len(nums)):
            if nums[i] % 2:
                a += 1
            else:
                b += 1
            if i and (nums[i-1] + nums[i]) % 2:
                c += 1
        # print(a, b, c)
        return max(a, b, c)