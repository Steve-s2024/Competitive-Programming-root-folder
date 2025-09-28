# boring simulation question: 41%
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        arr = [(0, i, i) for i in range(m)]
        ans = [-1] * m
        for i in range(n):
            tmp = []
            for j in range(len(arr)):
                r, c, id_ = arr[j]
                if grid[r][c] == 1 and c + 1 < m and grid[r][c + 1] == 1:
                    tmp.append((r + 1, c + 1, id_))
                if grid[r][c] == -1 and c - 1 >= 0 and grid[r][c - 1] == -1:
                    tmp.append((r + 1, c - 1, id_))
            arr = tmp

        for r, c, id_ in arr:
            ans[id_] = c
        return ans
