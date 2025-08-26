# couldn't optimize it
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        graph = [[None] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                for R in range(row):
                    for C in range(col):
                        if R == r and C == c: continue
                        if graph[r][c] == None: graph[r][c] = []
                        if (R, C) == (r + 1, c) or (R, C) == (r, c + 1):
                            graph[r][c].append((R, C, 1))
                        if grid[r][c] >= grid[R][C]:
                            graph[r][c].append((R, C, 2))

        minheap = [(0, 0, 0, k)]
        dp = [[None] * col for _ in range(row)]
        dp[0][0] = (0, k)
        while minheap:
            cost, r, c, k = heapq.heappop(minheap)
            if r == row - 1 and c == col - 1: return cost
            for R, C, typ in graph[r][c]:

                if typ == 1:
                    newC = cost + grid[R][C]
                    newK = k
                else:
                    if not k: continue
                    newC = cost
                    newK = k - 1
                if dp[R][C] != None and dp[R][C][0] <= newC and dp[R][C][1] >= newK: continue
                dp[R][C] = (newC, newK)
                heapq.heappush(minheap, (newC, R, C, newK))


