# a recursive function, which the base case is just a guess, will not work if the constraint get raised higher: 15%

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def recursive(i, status, sm):
            nonlocal k
            if sm > (1<<32): return 0
            res = (1 if sm == k else 0)
            res += recursive(i+1, True, sm+(1<<i))
            if status and sm > 0: res += recursive(i, False, sm-1)
            return res

        return recursive(0, True, 1)