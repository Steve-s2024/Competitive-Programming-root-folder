# fking wasting time trying to optimize it when it is clearly the intended solution: MLE
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        @cache
        def recursive(zero, one, prevZero, prevOne):
            nonlocal limit, MOD
            if zero == 0 and one == 0: return 1
            res = 0
            if prevOne <= limit and zero:
                res += recursive(zero-1, one, 1, prevOne+1)
            if prevZero <= limit and one:
                res += recursive(zero, one-1, prevZero+1, 1)
            return res % MOD
        return recursive(zero, one, 1, 1)