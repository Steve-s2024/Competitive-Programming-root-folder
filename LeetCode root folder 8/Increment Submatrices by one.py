# ultimate complicated and unintuitive 2D difference array + 2D prefix sum combination to achieve true linear solution
# : 95%
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        for t, l, b, r in queries:
            grid[t][l] += 1
            if b < n - 1: grid[b + 1][l] -= 1
            if r < n - 1: grid[t][r + 1] -= 1
            if b < n - 1 and r < n - 1: grid[b + 1][r + 1] += 1

        # for r in grid: print(r)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            tot = 0
            for j in range(n):
                tot += grid[i][j]
                ans[i][j] = tot

        for j in range(n):
            tot = 0
            for i in range(n):
                tot += ans[i][j]
                ans[i][j] = tot

        # for r in ans: print(r)
        return ans


# brute force difference array solution: 5%
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        for i in range(n):
            arr = [0] * n
            for t, l, b, r in queries:
                if i in range(t, b + 1):
                    arr[l] += 1
                    if r < n - 1: arr[r + 1] -= 1

            tot = 0
            for j in range(n):
                tot += arr[j]
                grid[i][j] = tot

        return grid

# a slightly better implementation of the same approach: 39%
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        for t, l, b, r in queries:
            for i in range(t, b + 1):
                grid[i][l] += 1
                if r < n - 1: grid[i][r + 1] -= 1

        for i in range(n):
            for j in range(1, n):
                grid[i][j] += grid[i][j - 1]

        return grid