# dfs brute force, no clue what to do what so ever: TLE
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        minPath = float('inf')
        def dfs(r, c, pathLen, remain):
            nonlocal minPath, row, col
            if pathLen >= minPath:
                return
            if r == row-1 and c == col-1:
                minPath = pathLen
                return 

            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if R in range(row) and C in range(col):
                    if grid[R][C] == 1:
                        if remain and (R, C) not in visited:
                            visited.add((R, C))
                            dfs(R, C, pathLen+1, remain-1)
                            visited.remove((R, C))
                    else:
                        if (R, C) not in visited:
                            visited.add((R, C))
                            dfs(R, C, pathLen+1, remain)
                            visited.remove((R, C))

        visited.add((0, 0))
        dfs(0, 0, 0, k)
        return minPath if minPath != float('inf') else -1



