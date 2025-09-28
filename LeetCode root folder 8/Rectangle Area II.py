# line sweep approach, can be used as template for most cases: 64%
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def helper(val):
            if not val: return 0
            # note, val[i] will be in the form (weight, l, r)
            # we only care about the interval (l, r), not the weight
            arr = sorted([(e[1], e[2]) for e in val])
            L, R = 0, 0
            res = 0
            for l, r in arr:
                if l <= R:
                    R = max(R, r)
                else:
                    res += R - L
                    L, R = l, r
            res += R - L
            return res

        MOD = 10 ** 9 + 7
        arr = rectangles
        arr.sort()
        arr.append((10 ** 9, 0, 10 ** 9, 0))
        minheap = []
        res = 0
        prev, cur = 0, 0
        for x1, y1, x2, y2 in arr:
            while minheap and minheap[0][0] <= x1:
                cur = minheap[0][0]
                res += (cur - prev) * helper(minheap)
                res %= MOD
                prev = cur
                heappop(minheap)
            cur = x1
            res += (cur - prev) * helper(minheap)
            res %= MOD
            prev = cur
            heappush(minheap, (x2, y1, y2))

        return res