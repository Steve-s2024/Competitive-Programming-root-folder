# Floyd-Warshall solution: 39%

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[inf] * n for _ in range(n)]

        for u, v, w in edges:
            dp[u][v] = min(dp[u][v], w)
            dp[v][u] = min(dp[v][u], w)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        mp = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if dp[i][j] <= distanceThreshold:
                    mp[i] += 1
        mi, idx = inf, 0
        for i in range(n):
            if mp[i] <= mi:
                mi = mp[i]
                idx = i
        return idx



