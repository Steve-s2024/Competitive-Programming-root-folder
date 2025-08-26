# no wonder its rated low, fking brute force passed so easily... I was overcomplicating it: 24%
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        tot = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0: tot += 1
        dp = {}
        cnt = 0
        vis = set()
        def dfs(r, c):
            nonlocal row, col, cnt
            if grid[r][c] == 2: return 1 if tot == cnt-1 else 0
            res = 0
            for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if R in range(row) and C in range(col) and grid[R][C] != -1 and (R, C) not in vis:
                    vis.add((R, C))
                    cnt += 1
                    res += dfs(R, C)
                    cnt -= 1
                    vis.remove((R, C))
            return res

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    vis.add((r, c))
                    return dfs(r, c)



# WA
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        tot = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0: tot += 1
        mask = 0
        dp = {}
        cnt = 0
        def dfs(r, c):
            nonlocal row, col, mask, cnt
            if grid[r][c] == 2: return 1 if tot == cnt else 0
            if (r, c, mask) in dp: return dp[(r, c, mask)]
            res = 0
            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if R in range(row) and C in range(col) and grid[R][C]!=-1 and mask&(1<<(col*r+c)) != 1<<(col*r+c):
                    mask ^= 1<<(col*r+c)
                    cnt += 1
                    res += dfs(R, C)
                    cnt -= 1
                    mask ^= 1<<(col*r+c)
            dp[(r, c, mask)] = res
            return res

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    mask ^= 1<<(col*r+c)
                    return dfs(r, c)