# bfs solution (bfs is really handy when comes to finding the shortest path!):435
# ms
# Beats
# 5.09%
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        minLen = 1
        q = deque([(0, 0)])
        row, col = len(grid), len(grid[0])
        visited = set()
        visited.add((0,0))
        while q:
            l = len(q)
            while l:
                [r, c] = q.popleft()
                if r == row-1 and c == col-1:
                    return minLen
                nextCoors = [(r+1, c), (r+1, c+1), (r, c+1), (r-1, c+1), (r-1, c), (r-1, c-1),(r, c-1),(r+1, c-1)]
                for R, C in nextCoors:
                    if (
                        R in range(row) and
                        C in range(col) and
                        (R, C) not in visited and
                        grid[R][C] != 1
                    ):
                        visited.add((R, C))
                        q.append((R, C))

                l -= 1
            minLen += 1
        return -1