# easy power and bit manipulation: 100%
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        a, b = (n + 1) // 2, n // 2

        res = 1
        # res = 5^a * 4^b

        bi = str(bin(a))[2:][::-1]
        tmp = 5
        for i in range(len(bi)):
            if bi[i] == '1':
                res *= tmp
                res %= mod
            tmp *= tmp
            tmp %= mod

        bi = str(bin(b))[2:][::-1]
        tmp = 4
        for i in range(len(bi)):
            if bi[i] == '1':
                res *= tmp
                res %= mod
            tmp *= tmp
            tmp %= mod

        return res
