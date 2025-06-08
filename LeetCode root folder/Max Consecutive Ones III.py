# sliding window solution:59
# ms
# Beats
# 73.49%
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        count = 0
        res = 0
        while r < len(nums):
            while r < len(nums) and nums[r] == 1:
                r += 1
            if r == len(nums):
                break

            if nums[r] == 0:
                count += 1
            if count > k:
                # print(l, r)
                # the current window without the rightmost element is the maximum window achievable if beginning from position l
                res = max(r - l, res)
                while count > k:
                    if nums[l] == 0:
                        count -= 1
                    l += 1
            r += 1

        return max(r - l, res)