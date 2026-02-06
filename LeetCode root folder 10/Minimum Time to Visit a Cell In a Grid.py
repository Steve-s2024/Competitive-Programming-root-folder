# so clever
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if min(grid[0][1], grid[1][0]) > 1: return -1
        hp = [(0, 0, 0)]
        vs = [[0]*m for _ in range(n)]
        while hp:
            t, r, c = heappop(hp)
            if vs[r][c]: continue
            vs[r][c] = 1
            if r == n-1 and c == m-1: return t

            for R, C in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if R in range(n) and C in range(m):
                    x = grid[R][C]
                    if x > t: heappush(hp, (x + (t-x+1)%2, R, C))
                    else: heappush(hp, (t+1, R, C))
