# finding the shortest path between every pair of vertex in the graph.
from math import inf
def floyedWarshall(n, edges):
    dp = [[inf] * n for _ in range(n)]
    for u, v, w in edges:
        dp[u][v] = w
        dp[v][u] = w
    for i in range(n): dp[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # now dp[i][j] will hold the shortest distance between node i and node j or inf if no such path exists.
    return dp

print(floyedWarshall(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]))
print(floyedWarshall(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]))




# a self wrote recursive implementation of the algorithm. all it is basically a complicated knapsack DP
def floyd(n, edges):
    mp = {}
    for u, v, w in edges:
        mp[(u, v)] = w
        mp[(v, u)] = w

    @cache
    def recursive(i, j, k):
        if k == -1: return mp[(i, j)] if (i, j) in mp else inf
        a = recursive(i, j, k-1)
        b = recursive(i, k, k-1) + recursive(k, j, k-1)
        return min(a, b)

    for i in range(n):
        for j in range(i+1, n):
            print(f'{i} -> {j}: {recursive(i, j, n-1)}')



floyd(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]])