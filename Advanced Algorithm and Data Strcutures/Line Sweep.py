# a line sweep approach for calculating rectangle area, the helper function lies the logic of vertical count in each
# horizontal moment. the val argument are expected to be the intervals representing the vertical image of the moment

from heapq import heappush, heappop

def lineSweep(arr):
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
    arr.sort()
    arr.append((10 ** 9, 0, 10 ** 9, 0)) # the 10**9 serves as a boundary element, make it bigger if necessary. but don't use inf.
    minheap = []
    res = 0
    prev, cur = 0, 0
    for x1, y1, x2, y2 in arr:
        while minheap and minheap[0][0] <= x1:
            cur = minheap[0][0]
            res += (cur - prev) * helper(minheap)
            prev = cur
            heappop(minheap)
        cur = x1
        res += (cur - prev) * helper(minheap)
        prev = cur
        heappush(minheap, (x2, y1, y2))

    return res


print(lineSweep([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
print(lineSweep([[0,0,1000000000,1000000000]]))