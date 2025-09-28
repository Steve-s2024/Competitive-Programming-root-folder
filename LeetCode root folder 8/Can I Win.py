# I voted down this solution when it first came to my head thinking it will TLE, but somehow it didn't, and took
# lot less time than anticipated: 66%
# the reason is not obvious, but it's because the mask itself contains the information of the total sum so far. So,
# there don't need to be a total sum so far in the DP state.
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0: return True
        n = maxChoosableInteger
        if sum(i for i in range(1, n + 1)) < desiredTotal: return False

        @cache
        def recursive(mask, f, tot):
            nonlocal n, desiredTotal
            if tot >= desiredTotal: return not f
            for i in range(1, n + 1):
                if mask & (1 << i): continue
                if recursive(mask | (1 << i), not f, tot + i) == f: return f
            return not f

        return recursive(0, True, 0)