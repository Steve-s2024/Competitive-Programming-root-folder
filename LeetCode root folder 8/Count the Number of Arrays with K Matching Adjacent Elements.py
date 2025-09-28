# trying to understand the derivation of this theorem (FLT), but never click: 5%
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        a, b = n - 1, 1
        res = m * pow(m - 1, n - k - 1, MOD) % MOD
        for i in range(k):
            res *= a
            res *= pow(b, MOD-2, MOD)
            res %= MOD
            a -= 1
            b += 1
        return res



# must use the fermat's little theorem for efficiency: TLE
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        a, b = n - 1, 1
        res = m * pow(m - 1, n - k - 1, MOD)
        for i in range(k):
            res *= a
            res *= pow(b, MOD-2, MOD)
            res %= MOD
            a -= 1
            b += 1
        return res



