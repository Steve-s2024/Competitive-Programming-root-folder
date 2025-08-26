# 43% same as old submission
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def recursive(mask, idx):
            nonlocal n
            res = 0
            for i in range(n):
                for j in range(i+1, n):
                    if i != j and mask&(1<<i) == 0 and mask&(1<<j) == 0:
                        a = recursive(mask^(1<<i)^(1<<j), idx+1) + idx*gcd(nums[i], nums[j])
                        res = max(a, res)
            return res
        return recursive(0, 1)