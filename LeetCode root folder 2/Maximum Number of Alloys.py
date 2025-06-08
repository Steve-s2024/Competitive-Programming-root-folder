# looks daunting, but easy to come up with brute force and then
# binary search solution: 32%
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0
        for comp in composition:
            maxCnt = 0
            l, r = 0, budget + max(stock)
            while l <= r:
                m = (l+r)//2
                totalCost = 0
                for i in range(n):
                    totalCost += max(0, m*comp[i] - stock[i])*cost[i]
                if totalCost > budget:
                    r = m-1
                else:
                    maxCnt = m
                    l = m+1
            # print(comp, maxCnt)
            res = max(res, maxCnt)
        return res