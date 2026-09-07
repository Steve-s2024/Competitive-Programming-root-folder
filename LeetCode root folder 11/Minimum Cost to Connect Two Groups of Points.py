# ill give it a 2300 at most


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])


        @cache
        def fn(i, msk):
            if i >= n:
                t = 0
                for j in range(m):
                    if msk&(1<<j) == 0:
                        mi = 1<<31
                        for I in range(n): mi = min(mi, cost[I][j])
                        t += mi
                return t


            res = 1<<31
            for j in range(m):
                a = fn(i+1, msk|(1<<j)) + cost[i][j]
                res = min(res, a)
            return res


        return fn(0, 0)


