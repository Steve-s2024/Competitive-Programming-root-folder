# easy simulation, with two pointers: 97%
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        badPair = 0
        ans = []
        l, r = 0, 1
        while r < k:
            if nums[r] != nums[r-1]+1:
                badPair+=1
            r += 1
        if badPair == 0:
            ans.append(nums[r-1])
        else:
            ans.append(-1)
        while r < n:
            if nums[r] != nums[r-1]+1:
                badPair+=1
            if nums[l]+1 != nums[l+1]:
                badPair-=1
            if badPair == 0:
                ans.append(nums[r])
            else:
                ans.append(-1)
            r+=1
            l+=1
        return ans
