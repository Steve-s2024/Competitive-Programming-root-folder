# 6%
class Solution:
    @staticmethod
    def getCoors(grid, r1, c1, r2, c2):
        n = len(grid)
        coors = [(r1+1, c1, r2+1, c2), (r1, c1+1, r2, c2+1)]
        if (
            r1 == r2 and
            r1+1 in range(n) and
            c1+1 in range(n) and
            grid[r1+1][c1] + grid[r1+1][c1+1] == 0
        ):
            coors.append((r1, c1, r1+1, c1))
        if (
            c1 == c2 and
            r1+1 in range(n) and
            c1+1 in range(n) and
            grid[r1][c1+1] + grid[r1+1][c1+1] == 0
        ):
            coors.append((r1, c1, r1, c1+1))
        return coors


    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set()
        vis.add((0, 0, 0, 1))
        q = deque([(0, 0, 0, 1)])
        cnt = 0

        while q:
            for _ in range(len(q)):
                r1, c1, r2, c2 = q.popleft()
                if (r1, c1) == (n-1, n-2) and (r2, c2) == (n-1, n-1):
                    return cnt
                coors = Solution.getCoors(grid, r1, c1, r2, c2)
                for R1, C1, R2, C2 in coors:
                    if (
                        R1 in range(n) and C1 in range(n) and
                        R2 in range(n) and C2 in range(n) and
                        grid[R1][C1] != 1 and grid[R2][C2] != 1 and
                        (R1, C1, R2, C2) not in vis
                    ):
                        vis.add((R1, C1, R2, C2))
                        q.append((R1, C1, R2, C2))
            cnt += 1
        return -1