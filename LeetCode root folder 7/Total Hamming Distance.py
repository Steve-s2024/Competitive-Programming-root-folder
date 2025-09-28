# bit manipulation, break down the bits: 5%
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mp = [0]*30
        res = 0
        for i in range(n):
            num = nums[i]
            for j in range(30):
                if num%2: res += i-mp[j]
                else: res += mp[j]
                mp[j] += num%2
                num >>= 1
        return res