# I would've never thought of this approach, this is around 2400-2500 (credit: neetcode)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def recursive(l, r):
            if l > r: return 0
            res = 0
            a, c = nums[l-1] if l else 1, nums[r+1] if r < n-1 else 1
            for i in range(l, r+1):
                b = nums[i]
                res = max(res, recursive(l, i-1) + recursive(i+1, r) + a*b*c)
            return res

        return recursive(0, n-1)