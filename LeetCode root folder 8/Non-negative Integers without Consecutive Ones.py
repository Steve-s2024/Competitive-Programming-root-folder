# digit DP: 24%

class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n))[2:]
        @cache
        def recursive(i, lim, prv):
            if i >= len(s): return 1
            res = 0
            mx = int(s[i]) if lim else 1
            res += recursive(i+1, 1 if lim and mx==0 else 0, 0)
            if not prv and 1<=mx: res += recursive(i+1, lim, 1)
            return res
        return recursive(0, 1, 0)

