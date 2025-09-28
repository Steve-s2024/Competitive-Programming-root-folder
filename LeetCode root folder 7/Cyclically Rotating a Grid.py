# super boring and tedious one: 20%
class Solution:
    def helper(self, grid, t, l, b, r):
        i, j = t, l
        res = []
        drct = (0, 1)
        f = 1
        while 1:
            if (i, j) == (t, l):
                if f:
                    f = 0
                else:
                    break
                drct = (0, 1)
            if (i, j) == (t, r): drct = (1, 0)
            if (i, j) == (b, r): drct = (0, -1)
            if (i, j) == (b, l): drct = (-1, 0)
            res.append(grid[i][j])
            i, j = i + drct[0], j + drct[1]
        return res

    def helper2(self, grid, t, l, b, r, arr):
        i, j = t, l
        drct = (0, 1)
        f = 1
        cnt = 0
        while 1:
            if (i, j) == (t, l):
                if f:
                    f = 0
                else:
                    break
                drct = (0, 1)
            if (i, j) == (t, r): drct = (1, 0)
            if (i, j) == (b, r): drct = (0, -1)
            if (i, j) == (b, l): drct = (-1, 0)
            grid[i][j] = arr[cnt]
            cnt += 1
            i, j = i + drct[0], j + drct[1]

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        arrs = []
        t, l, b, r = 0, 0, n - 1, m - 1
        while t <= b and l <= r:
            arrs.append(self.helper(grid, t, l, b, r))
            t, l, b, r = t + 1, l + 1, b - 1, r - 1

        # print(arrs)
        for i in range(len(arrs)):
            rot = k % len(arrs[i])
            arrs[i] = arrs[i][rot:] + arrs[i][:rot]

        cnt = 0
        t, l, b, r = 0, 0, n - 1, m - 1
        while t <= b and l <= r:
            arrs.append(self.helper2(grid, t, l, b, r, arrs[cnt]))
            t, l, b, r = t + 1, l + 1, b - 1, r - 1
            cnt += 1
        return grid

