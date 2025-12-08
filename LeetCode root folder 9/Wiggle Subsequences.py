# ~1200 on codeforces, boring
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(f):
            res = 1
            cr = nums[0]
            x = 1
            for i in range(1, n):
                if f == 1: # find next smaller
                    if nums[i] < cr:
                        x+=1
                        f = 0
                    cr = nums[i]
                else: # find next bigger
                    if nums[i] > cr:
                        x+=1
                        f = 1
                    cr = nums[i]
                res = max(res, x)
            return res
        return max(helper(1), helper(0))