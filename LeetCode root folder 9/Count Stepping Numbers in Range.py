# this feels weirdly straight forward. though the implementation and state transition can be painful, but it does not
# deserve to be 2350

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 10**9 + 7
        n = len(high)
        low = low.zfill(n)
        # print(low, high)
        @cache
        def recursive(i, bf, lf, hf, prv):
            nonlocal n, mod
            if i >= n: return 1
            res = 0
            lw, hi = 0 if not lf else int(low[i]), 9 if not hf else int(high[i])
            # print(i, bf, lf, hf, prv, lw, hi)
            if bf:
                for j in range(lw, hi + 1):
                    a = recursive(i + 1, not j, lf and j == lw, hf and j == hi, j)
                    res += a
                    # print(i, j, a)
            else:
                for j in [prv-1, prv+1]:
                    if hf and j > hi or lf and j < lw or j not in range(10): continue
                    res += recursive(i + 1, 0, lf and j == lw, hf and j == hi, j)
            return res % mod
        return recursive(0, 1, 1, 1, 0)

