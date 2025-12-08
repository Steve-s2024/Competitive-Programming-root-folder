# damn pretty easy map counting solution.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        res = 0
        n = len(points)
        for i in range(n):
            x, y = points[i]
            mp = defaultdict(int)
            for j in range(n):
                if j == i: continue
                xx, yy = points[j]
                slp = inf if y == yy else ((x-xx)/(y-yy))
                mp[slp] += 1
            res = max(res, max(mp.values())+1)
        return res