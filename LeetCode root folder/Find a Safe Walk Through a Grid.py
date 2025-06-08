# brute-force: tle
'''class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (
                r not in range(row) or
                c not in range(col) or
                (r, c) in visited
            ):
                return float('inf')
            if r == row-1 and c == col-1:
                return grid[r][c]
            visited.add((r, c))
            minCost = min(
                dfs(r+1, c),
                dfs(r-1, c),
                dfs(r, c+1),
                dfs(r, c-1)
            )
            visited.remove((r, c))
            return minCost + grid[r][c]
        return dfs(0, 0) < health'''

# optimized brute force: tle
'''class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c, cost):
            nonlocal row, col
            if (
                r not in range(row) or
                c not in range(col) or
                (r, c) in visited
            ):
                return False
            cost += grid[r][c]
            if cost >= health:
                return False
            if r == row - 1 and c == col - 1:
                return True
            visited.add((r, c))
            res = (
                dfs(r+1, c, cost) or
                dfs(r-1, c, cost) or
                dfs(r, c+1, cost) or
                dfs(r, c-1, cost)
            )
            visited.remove((r, c))
            return res
        return dfs(0, 0, 0)
'''

# this is hard, but once you've found out the relationship of this question with the "min time for signal to travel
# to all nodes" question and its use of min heap to keep track of time, the answer is very clear -> Dijkstra's algorithm:
# 167
# ms
# Beats
# 55.96%
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()
        visited.add((0, 0))
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        while minHeap:
            cur = heapq.heappop(minHeap)
            t, r, c = cur[0], cur[1], cur[2]
            if r == row - 1 and c == col - 1:
                # print(t)
                return t < health
            steps = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for newR, newC in steps:
                if (
                        newR in range(row) and
                        newC in range(col) and
                        (newR, newC) not in visited
                ):
                    visited.add((newR, newC))
                    heapq.heappush(minHeap, (t + grid[newR][newC], newR, newC))

