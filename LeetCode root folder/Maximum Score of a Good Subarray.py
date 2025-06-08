# why am i so goddamn genious? why my idea is always 
# correct? two pointer spread from k, and greedily
# test out all the subarray candidates: 96.81% 
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = k-1, k+1
        min_ = nums[k]

        res = nums[k]
        while l >= 0 or r < n:
            
            if l >= 0 and (r >= n or nums[l] >= nums[r]):
                min_ = min(min_, nums[l])
                while l > 0 and nums[l-1] >= nums[l]:
                    l -= 1
                l -= 1
            else:
                min_ = min(min_, nums[r])
                while r < n-1 and nums[r+1] >= nums[r]:
                    r += 1
                r += 1
            
            size = r-l-1
            score = min_ * size
            res = max(res, score)
        return res
            