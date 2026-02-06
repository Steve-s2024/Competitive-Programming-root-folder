# thinking a bit longer with the diagonal length and intersection of diagonals of rectangle, we can pick arbitrary two
# points and use map to iterate over all other points on the same circle (originate from midpoint of diagonal and
# contains the two points picked), this will probably give average O(n^2) performance.

# boring, just need an insight into vector geometry
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        st = set()
        for p in points: st.add(tuple(p))
        res = inf
        for a in points:
            for b in points:
                for c in points:
                    d = (a[0] + b[0]-a[0] + c[0]-a[0], a[1] + b[1]-a[1] + c[1]-a[1])
                    if d not in st: continue
                    if (
                        (a[0]-b[0])*(c[1]-d[1]) == (c[0]-d[0])*(a[1]-b[1]) and
                        (a[0]-c[0])*(b[1]-d[1]) == (b[0]-d[0])*(a[1]-c[1]) and
                        (a[0]-b[0])*(a[0]-c[0]) + (a[1]-b[1])*(a[1]-c[1]) == 0
                    ):
                        w, l = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2), sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
                        if w*l: res = min(res, w*l)
        return res if res != inf else 0