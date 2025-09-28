# first ever working logtrick solution! yeah😁: 89%
# didn't have to change much from the solution below
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        res = 0
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[j] & nums[i] == nums[j]: break
                nums[j] &= nums[i]
            while l <= i and nums[l] < k: l += 1
            while r <= i and nums[r] <= k : r += 1
            if l >= n or nums[l] > k: continue
            res += r-l
        return res


# I thought it asked for OR, so I wrote this logtrick solution. and then realize it's about AND...
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        res = 0
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[j] | nums[i] == nums[j]: break
                nums[j] |= nums[i]
            while l <= i and nums[l] > k: l += 1
            while r <= i and nums[r] >= k : r += 1
            if l >= n or nums[l] < k: continue
            res += r-l
        return res

