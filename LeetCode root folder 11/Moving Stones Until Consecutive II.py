# show me the money biiiitch. score down on that olympic math level reasoning
class Solution:
    def numMovesStonesII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        a, b, c, d = nums[:2]+nums[-2:]
        mx = d-a+1 - n - min(b-a-1, d-c-1)


        mi = n
        j = 0
        for i in range(n):
            while j < n and nums[j]-nums[i]+1 <= n: j += 1
            x = n-(j-i)
            if nums[j-1]-nums[i]+1 == j-i and j-i == n-1: x += 1
            mi = min(mi, x)
        return [mi, mx]