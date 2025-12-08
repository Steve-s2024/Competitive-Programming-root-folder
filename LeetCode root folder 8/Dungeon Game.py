# dp solution, can be easily upgrade to bottom up. the logic of the transformation is not easy to figure out though
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0]*m for _ in range(n)]
        dp[-1][-1] = max(-dungeon[-1][-1], 0)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1: continue
                a, b = dp[i+1][j] if i < n-1 else inf, dp[i][j+1] if j < m-1 else inf
                if dungeon[i][j] < 0: dp[i][j] = -dungeon[i][j] + min(a, b)
                else: dp[i][j] = max(min(a, b)-dungeon[i][j], 0)
        return dp[0][0]+1