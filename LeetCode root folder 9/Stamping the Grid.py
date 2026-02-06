# all about sub matrix sum checking, 4 similar nested loops just to do the conversion of problem into standard
# sub-matrix sum query

class Solution:
    def possibleToStamp(self, g: List[List[int]], h: int, w: int) -> bool:
        n, m = len(g), len(g[0])
        # for r in g: print(r)

        mp = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                a = mp[i + 1][j] if i < n - 1 else 0
                b = mp[i][j + 1] if j < m - 1 else 0
                c = mp[i + 1][j + 1] if i < n - 1 and j < m - 1 else 0
                mp[i][j] = a + b - c + g[i][j]
        # for r in mp: print(r)

        mat = [[0] * m for _ in range(n)]
        for i in range(n - h, -1, -1):
            for j in range(m - w, -1, -1):
                if g[i][j] == 1: continue
                a = mp[i][j]
                b = mp[i + h][j] if i + h < n else 0
                c = mp[i][j + w] if j + w < m else 0
                d = mp[i + h][j + w] if i + h < n and j + w < m else 0
                if a - b - c + d == 0: mat[i + h - 1][j + w - 1] = 1  # good block
        # for r in mat: print(r)

        mp = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                a = mp[i + 1][j] if i < n - 1 else 0
                b = mp[i][j + 1] if j < m - 1 else 0
                c = mp[i + 1][j + 1] if i < n - 1 and j < m - 1 else 0
                mp[i][j] = a + b - c + mat[i][j]
        # for r in mp: print(r)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if g[i][j] == 1: continue
                a = mp[i][j]
                b = mp[i + h][j] if i + h < n else 0
                c = mp[i][j + w] if j + w < m else 0
                d = mp[i + h][j + w] if i + h < n and j + w < m else 0
                if a - b - c + d == 0: return False  # uncovered empty cell

        return True


