# absolutely bore the shit out of me
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        srcs = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: srcs.append((i, j))
        le, ri = 0, 10 ** 9
        res = -1

        while le <= ri:
            mid = (le + ri) // 2
            vs = [[0] * m for _ in range(n)]
            q = deque(srcs)
            x = mid+1
            while q and x:
                x -= 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if vs[r][c] == 1: continue
                    vs[r][c] = 1
                    for R, C in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                        if R in range(n) and C in range(m) and vs[R][C] == 0 and grid[R][C] == 0:
                            q.append((R, C))
            f = 0
            me = deque([(0, 0)])
            while me:
                tmp = set()
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if vs[r][c] == 1: continue
                    tmp.add((r, c))
                    vs[r][c] = 1
                    for R, C in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                        if R in range(n) and C in range(m) and vs[R][C] in [0,-1] and grid[R][C] == 0:
                            q.append((R, C))

                for _ in range(len(me)):
                    r, c = me.popleft()
                    if vs[r][c] == -1: continue
                    if vs[r][c] == 0: vs[r][c] = -1
                    for R, C in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                        if R == n - 1 and C == m - 1:
                            f = 1 if (vs[R][C] == 0 or vs[R][C] == 1 and (R, C) in tmp) else 0
                            break
                        if R in range(n) and C in range(m) and vs[R][C] == 0 and grid[R][C] == 0:
                            me.append((R, C))
                    if f: break
                if f: break

            if f:
                res = mid
                le = mid + 1
            else: ri = mid - 1
        return res