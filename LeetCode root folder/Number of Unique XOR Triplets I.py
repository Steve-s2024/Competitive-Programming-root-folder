# pure math quesiton... almost like on CF
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        n = len(nums)
        res = 1
        while res <= n:
            res *= 2
        return res 