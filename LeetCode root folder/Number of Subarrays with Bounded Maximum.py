# 7%
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        def findNumberOfValidSubarray(l, r):
            nonlocal left, right
            # print(l, r)
            size = r-l+1
            total = size*(size+1)//2
            i = l
            while i <= r:
                a, b = i, i
                while b < n and nums[b] < left:
                    b+=1
                s = b-a
                total-=s*(s+1)//2
                i=max(i+1, b)
            # print(total)
            return total
                
        
        l, r = 0, 0
        res = 0
        while r < n:
            while r < n and nums[r] <= right:
                r+=1
            if r > l:
                res += findNumberOfValidSubarray(l, r-1)
            l = r+1
            r = r+1
        return res