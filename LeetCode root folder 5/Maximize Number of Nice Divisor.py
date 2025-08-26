# not trivial math problem that require you simplify a hard problem into a very simple greedy problem: 13%

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        re = primeFactors % 3
        if re == 1 and primeFactors > 1:
            re = 4
            primeFactors -= 4
        else: primeFactors -= re

        # 3*3*3*3...
        tmp = 3
        MOD = 10**9 + 7
        primeFactors //= 3
        res = 1


        while primeFactors:
            if primeFactors&1:
                res *= tmp
                res %= MOD
            tmp *= tmp
            tmp %= MOD
            primeFactors >>= 1
        return (res*max(re, 1)) % MOD