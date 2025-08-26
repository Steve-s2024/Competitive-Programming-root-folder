# brute force BFS solution, simulate the whole process: 7%
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        src = (-1, -1)
        dst = (-1, -1)
        p = (-1, -1)
        row, col = len(grid), len(grid[0])
        len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'S': p = (i, j)
                if grid[i][j] == 'B': src = (i, j)
                if grid[i][j] == 'T': dst = (i, j)

        qq = deque([src + p])
        st = set()
        st.add(qq[0])

        def bfs(sr, sc, pr, pc):
            nonlocal row, col
            vis = set()
            vis.add((pr, pc))
            q = deque([(pr, pc)])
            while q:
                r, c = q.popleft()
                for R, C in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        R in range(row) and C in range(col) and
                        grid[R][C] != '#' and (R, C) != (sr, sc) and
                        (R, C) not in vis
                    ):
                        vis.add((R, C))
                        q.append((R, C))
            res = []
            coors = ((sr - 1, sc), (sr, sc + 1), (sr + 1, sc), (sr, sc - 1))  # ^ > v <
            for i in range(4):
                if coors[i] in vis: res.append(coors[(i + 2) % 4])
            return res

        res = 0
        while qq:
            for _ in range(len(qq)):
                sr, sc, pr, pc = qq.popleft()
                # print(sr, sc, pr, pc)
                if (sr, sc) == dst: return res
                coors = bfs(sr, sc, pr, pc)
                for r, c in coors:
                    nxt = (r, c, sr, sc)
                    if (
                        r in range(row) and c in range(col) and
                        grid[r][c] != '#' and nxt not in st
                    ):
                        st.add(nxt)
                        qq.append(nxt)
            res += 1
        return -1

