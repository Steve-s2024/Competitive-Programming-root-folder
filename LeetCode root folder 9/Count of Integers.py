# at most 2200 if one have not encountered digit dp before, otherwise it's a 2000 to 1900 problem
# this is seriously wrong to be rated 2350

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        n = len(num2)
        MOD = 10**9 + 7
        num1 = num1.zfill(n)
        @cache
        def recursive(i, lf, hf, dsm):
            nonlocal n, MOD
            if i >= n: return 1 if dsm in range(min_sum, max_sum+1) else 0

            lw = 0 if not lf else int(num1[i])
            hi = 9 if not hf else int(num2[i])
            res = 0
            for j in range(lw, hi+1):
                res += recursive(i+1, lf and j==lw, hf and j==hi, dsm+j)
                res %= MOD
            return res
        return recursive(0, 1, 1, 0)