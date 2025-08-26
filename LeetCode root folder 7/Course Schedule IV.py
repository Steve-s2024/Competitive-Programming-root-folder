# Floyd Warshall, very inefficient: 15%
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        n = numCourses
        dp = [[0] * n for _ in range(n)]
        for u, v in prerequisites:
            dp[u][v] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        ans = []
        for u, v in queries:
            if dp[u][v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans