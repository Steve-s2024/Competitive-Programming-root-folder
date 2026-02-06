# in first encounter I thought this is a supped up version of the cherry pickup problem (which is a nightmare)
# then realize the trap by the writer, once spotted the key constraint on number of moves to take, this problem is very brainless

class Solution:
    def maxCollectedFruits(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])

        @cache
        def fn(r, c):
            res = 0
            for R, C in ((r+1, c+1), (r, c+1), (r-1, c+1)):
                if R in range(n) and C in range(n) and C < R:
                    res = max(res, fn(R, C) + g[R][C])
            return res
        a = fn(n-1, 0)+g[n-1][0]

        @cache
        def dfs(r, c):
            res = 0
            for R, C in ((r+1, c+1), (r+1, c), (r+1, c-1)):
                if R in range(n) and C in range(n) and R < C:
                    res = max(res, dfs(R, C) + g[R][C])
            return res
        b = dfs(0, n-1)+g[0][n-1]
        # print(a, b)
        res = a+b
        for i in range(n): res += g[i][i]
        return res