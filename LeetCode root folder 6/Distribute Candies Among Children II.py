# hard one to uncover the trick, and this tricky solution is even far from the best approach: 42%
class Solution:
    @staticmethod
    def getNum(tot, lim):
        lo = tot - lim
        hi = lim
        if lo > hi: return 0

        if lo < 0:
            hi += lo
            lo -= lo
        size = hi-lo+1
        return size


    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit, n)+1):
            re = n-i
            a = Solution.getNum(re, limit)
            res += a
            # print(i, a)
        return res
