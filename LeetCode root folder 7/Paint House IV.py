# not very hard as its rating would suggest: 34%
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        @cache
        def recursive(prevI, i, j, prevJ):
            if i > j: return 0
            res = inf
            for iC in range(3):
                for jC in range(3):
                    if iC == jC or iC == prevI or jC == prevJ: continue
                    res = min(res, recursive(iC, i+1, j-1, jC) + cost[i][iC] + cost[j][jC])
            return res
        return recursive(-1, 0, n-1, -1)
