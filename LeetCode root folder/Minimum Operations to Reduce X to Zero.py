# prefix, suffix sum & hashing: 8%
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = 0
        hashMap = {}
        hashMap[0] = 0
        for idx, num in enumerate(nums):
            total += num
            hashMap[total] = idx+1
        
        n = len(nums)
        total = 0
        res = float('inf')
        if x in hashMap:
            res = hashMap[x]
        for i in range(n-1, -1, -1):
            total += nums[i]
            tar = x - total
            if tar in hashMap and hashMap[tar] <= i:
                res = min(res, hashMap[tar] + n-i)      
        if res == float('inf'):
            return -1
        return res      
