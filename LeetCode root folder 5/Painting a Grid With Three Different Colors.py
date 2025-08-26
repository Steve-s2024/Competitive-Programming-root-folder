# the idea is on the right track, but the implementation is very inefficient among the alternatives: 5%
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        def getComb(tup):
            res = []
            stk = []
            m = len(tup)

            def recursive(i):
                if i >= m:
                    res.append(stk[:])
                    return
                for j in range(3):
                    if j == tup[i] or stk and stk[-1] == j: continue
                    stk.append(j)
                    recursive(i + 1)
                    stk.pop()

            recursive(0)
            return res

        MOD = 10 ** 9 + 7

        @cache
        def recursive(i, tup):
            if i >= n: return 1
            res = 0
            for nxt in getComb(tup):
                res += recursive(i + 1, tuple(nxt))
                res %= MOD

            return res

        return recursive(0, tuple([-1] * m))
