# not hard for the logic, but to deal with the integer overflow and modulo operation, you actually need the knowledge
# of fermat's theorem to get the inverse modular of the denominator of each 'word' and multiply it with the numerator
# the theorem tells us that the modular inverse of b%m is b^(m-2), which is what I did in the last line of getNum: 68%
class Solution:
    @staticmethod
    def getNum(n, arr):
        MOD = 10 ** 9 + 7
        fn = 1
        for i in range(1, n + 1):
            fn *= i
            fn %= MOD
        farr = 1
        for val in arr:
            for i in range(1, val + 1):
                farr *= i
                farr %= MOD

        return (fn * pow(farr, MOD - 2, MOD)) % MOD

    def countAnagrams(self, s: str) -> int:
        res = 1
        MOD = 10 ** 9 + 7
        for word in s.split():
            mp = Counter(word)
            tot = Solution.getNum(len(word), list(mp.values()))
            res *= tot
            res %= MOD
        return int(res)


#TLE
class Solution:
    @staticmethod
    def getFac(num):
        res = 1
        for i in range(1, num+1): res *= i
        return res

    def countAnagrams(self, s: str) -> int:
        res = 1
        MOD = 10**9 + 7
        for word in s.split():
            mp = Counter(word)
            tot = Solution.getFac(len(word))
            for val in mp.values():
                for i in range(1, val+1): tot //= i
            res *= tot
            res %= MOD
        return res