# dp solution:167
# ms
# Beats
# 80.93%
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = grid[-1]
        for i in range(len(grid) - 2, -1, -1):
            tmp = []
            for j in range(len(grid[i])):
                minCost = float('inf')
                for k, cost in enumerate(moveCost[grid[i][j]]):
                    curCost = cost + dp[k]
                    minCost = min(minCost, curCost)
                tmp.append(minCost + grid[i][j])
            dp = tmp
        return min(dp)

