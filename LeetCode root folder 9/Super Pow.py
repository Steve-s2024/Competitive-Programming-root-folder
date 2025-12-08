# pretty interesting modular arithmetic problem, one of the best editorial i've made
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        x = 1
        n = len(b)
        for i in range(n):
            x *= pow(a, b[i])
            x %= mod
            if i == n-1: break
            t = x
            x = 1
            for j in range(10):
                x *= t
                x %= mod
        return x