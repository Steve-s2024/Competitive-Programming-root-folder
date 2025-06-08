# this is some crazy question, not even easy to come 
# down on the solution, and even harder to implement 
# the modulo... I experienced modulo brainstorming:100%
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        MOD = 1000000007
        x = pow(2, p)
        cap = x//2
        i = 1
        tar = x-2
        res = tar
        # print(cap)
        while i < cap//2:
            tar *= tar 
            res *= tar
            tar %= MOD
            res %= MOD
            i *= 2
        res *= (x-1)
        return res % MOD 

# the optimized one, time complexity worked, but
# i just can't figure out how to work around the 
# modulo, and the code will fail.
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        MOD = 1000000007
        x = pow(2, p)
        cap = x//2
        i = 1 
        tar = x-2
        # print(cap)
        while i < cap:
            tar *= tar 
            tar %= MOD
            i *= 2
        tar //= (x-2)
        tar *= (x-1)
        return tar % MOD


# crazy thing is this code get time limit exceed: TLE
# imageine how crazy this question must be haha
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        x = pow(2, p)
        return (pow(x-2, x//2-1) * (x-1)) % 1000000007