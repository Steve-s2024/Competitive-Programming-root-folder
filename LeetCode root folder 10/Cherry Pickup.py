# TLE
# this is my new nightmare, no clue how to reduce the time complexity (been trying it from time to time over months)
class Solution:
    def cherryPickup(self, g: List[List[int]]) -> int:
        n = len(g)
        @cache
        def fn(i, i1, i2):
            nonlocal n
            if i >= n: return 0 if i1 == i2 == n - 1 else -inf
            res = -inf
            j1 = i1
            x = 0
            while j1 < n and g[i][j1] != -1:
                x += g[i][j1]
                j2 = i2
                y = 0
                while j2 < n and g[i][j2] != -1:
                    if j2 not in range(i1, j1 + 1): y += g[i][j2]
                    if i == n-1 or (g[i+1][j2] != -1 and g[i+1][j1] != -1): res = max(res, fn(i + 1, j1, j2) + x+y)
                    j2 += 1
                j1 += 1
            return res

        res = fn(0, 0, 0)
        return res if res != -inf else 0