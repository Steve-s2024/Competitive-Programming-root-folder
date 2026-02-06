#  27ms beats 99.19% lol, how is this so fast? classic digit dp with tricks, x for odd even verification, re for remainder verification
# the trick is the modular trick of "computing the current remainder from previous one".
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        high = str(high)
        n = len(high)
        low = str(low).zfill(n)

        @cache
        def recursive(i, lf, hf, bf, re, x):
            nonlocal n, k
            if i >= n: return 1 if x == 0 and re == 0 else 0
            lw = 0 if not lf else int(low[i])
            hi = 9 if not hf else int(high[i])
            res = 0
            for j in range(lw, hi + 1):
                if bf and j == 0:
                    res += recursive(i + 1, lf and j == lw, hf and j == hi, 1, re, x)
                else:
                    nre, nx = (re * 10 + j) % k, x + (1 if j % 2 else -1)
                    res += recursive(i + 1, lf and j == lw, hf and j == hi, 0, nre, nx)

            return res

        return recursive(0, 1, 1, 1, 0, 0)

