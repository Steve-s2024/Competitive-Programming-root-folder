



# failed DFS DP attempt
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row, col = len(points), len(points[0])
        vis = set()
        dp = {}
        def recursive(r, c):
            nonlocal row, col
            if r >= row: return 0
            if (r, c) in dp: return dp[(r, c)]
            res = -float('inf')
            if c < col - 1 and (r, c + 1) not in vis:
                vis.add((r, c + 1))
                tot = recursive(r, c + 1)
                res = max(res, tot - 1)
                vis.remove((r, c + 1))
            if c > 0 and (r, c - 1) not in vis:
                vis.add((r, c - 1))
                tot = recursive(r, c - 1)
                res = max(res, tot - 1)
                vis.remove((r, c - 1))
            tot = recursive(r + 1, c) + points[r][c]
            res = max(res, tot)
            dp[(r, c)] = res
            return res

        recursive(0, 0)

        print(dp)
        return max(dp[(0, c)] for c in range(col))

