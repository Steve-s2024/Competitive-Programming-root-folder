# pretty standard multidimensional pick or not pick DP. does not deserve its rating (2403)
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        @cache
        def fn(i, gcd1, gcd2):
            nonlocal mod, n
            if i >= n: return 1 if gcd1 == gcd2 and gcd1 != -1 else 0
            res = fn(i + 1, gcd1, gcd2)
            if gcd1 == -1:
                res += fn(i + 1, nums[i], gcd2)
            else:
                res += fn(i + 1, gcd(gcd1, nums[i]), gcd2)
            if gcd2 == -1:
                res += fn(i + 1, gcd1, nums[i])
            else:
                res += fn(i + 1, gcd1, gcd(gcd2, nums[i]))
            return res % mod

        return fn(0, -1, -1)
