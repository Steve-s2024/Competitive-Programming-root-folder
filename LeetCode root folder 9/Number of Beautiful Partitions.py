# partition type of DP, feels quite comfortable dealing with them

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        mod = 10 ** 9 + 7

        @cache
        def recursive(i, K, f):
            nonlocal n, mod
            if i >= n: return 1 if f == K == 0 else 0
            res = 0
            if f == 1: res = recursive(i + 1, K, f)
            if f == 0 and s[i] in '2357' and K: res += recursive(i + minLength - 1, K, 1)
            if f == 1 and s[i] in '14689': res += recursive(i + 1, K - 1, 0)
            return res % mod

        return recursive(0, k, 0)
