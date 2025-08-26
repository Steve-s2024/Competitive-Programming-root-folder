# boring brute force DP solution: 49%
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def recursive(pos, mask):
            nonlocal n
            res = 0
            for i in range(n):
                for j in range(i+1, n):
                    if not mask&(1<<i) and not mask&(1<<j):
                        a = recursive(pos+1, mask^(1<<i)^(1<<j)) + pos*math.gcd(nums[i], nums[j])
                        res = max(res, a)
            return res
        return recursive(1, 0)