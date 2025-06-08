# hardly hard while knowing Dijkstra
# : 18%
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        heapq.heapify(minHeap)
        visited = set()
        res = 0
        row, col = len(grid), len(grid[0])
        while minHeap:
            cur, r, c = heapq.heappop(minHeap)
            res = max(res, cur)
            if r == row-1 and c == col-1:
                break
            if (r, c) not in visited:
                visited.add((r, c))
                for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if R in range(row) and C in range(col):
                        val = grid[R][C]
                        heapq.heappush(minHeap, (val, R, C))
        return res