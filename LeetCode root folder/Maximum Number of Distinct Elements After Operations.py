# greedy 48%
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        res, tmp = 0, nums[0]-k
        n = len(nums)
        while i < n:
            tmp = max(tmp, nums[i]-k)
    
            while i < n-1 and nums[i] == nums[i+1]:
                if tmp <= nums[i]+k:
                    res+=1
                    tmp+=1 
                i+=1
            
            if tmp <= nums[i]+k:
                res+=1
                tmp+=1
            i+=1
        return res

