# binary search and bfs solution: 5%
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = [(r - 1, c - 1) for r, c in cells]
        n = len(cells)
        left, right = 0, n - 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            grid = [[0] * col for _ in range(row)]
            for r, c in cells[:mid + 1]: grid[r][c] = 1

            q = deque()
            vis = set()
            for i in range(col):
                if grid[0][i] == 0:
                    vis.add((0, i))
                    q.append((0, i))

            flag = False
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    flag = True
                    break
                for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if R in range(row) and C in range(col) and grid[R][C] != 1 and (R, C) not in vis:
                        vis.add((R, C))
                        q.append((R, C))

            for rr in grid: print(rr)
            if flag:
                res = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return res