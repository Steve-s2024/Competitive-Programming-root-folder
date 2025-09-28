# couldn't figure out the logtrick approach, but close. also learned a lot about logtrick

# brute force, before logtrick: TLE
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        for i in range(n-1, -1, -1):
            mx = nums[i]
            size = 1
            for j in range(i+1, n):
                if nums[i]|nums[j] > mx:
                    mx = nums[i]|nums[j]
                    size = j-i+1
                nums[j] |= nums[i]
            ans[i] = size
        return ans