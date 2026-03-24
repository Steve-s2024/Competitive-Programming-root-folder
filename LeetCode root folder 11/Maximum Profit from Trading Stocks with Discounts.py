# run time too strict. this O(n^3) solution should be accepted
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            u, v = u - 1, v - 1
            g[u].append(v)

        @cache
        def fn(u, i, b, f1, f2):
            res = 0
            cst = present[u] // (2 if f1 else 1)
            if not f2 and b >= cst: res = max(res, fn(u, i, b - cst, f1, 1) + future[u] - cst)
            if i >= len(g[u]): return res

            for j in range(b + 1):
                a = fn(u, i + 1, b - j, f1, f2) + fn(g[u][i], 0, j, f2, 0)
                res = max(res, a)

            return res

        fn.cache_clear()
        return fn(0, 0, budget, 0, 0)