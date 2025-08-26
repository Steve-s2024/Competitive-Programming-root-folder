# got dumped into several corner, then realize this can be cleverly solved by the simple standard Dijkstra when you
# view it in a complete different angle: 20%
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        minheap = [(0, 0, 0)]
        vis = set()
        while minheap:
            cnt, r, c = heapq.heappop(minheap)
            if r == row - 1 and c == col - 1: return cnt
            for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if R in range(row) and C in range(col) and (R, C) not in vis:
                    vis.add((R, C))
                    heapq.heappush(minheap, (cnt + grid[R][C], R, C))

