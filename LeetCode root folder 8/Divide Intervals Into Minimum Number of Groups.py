# two ways of approach, in this case using minheap is faster, but sometimes the difference array can fast due the
# it's linear property: 9%, 38%
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        mx = max(e[1] for e in intervals)
        arr = [0] * (mx + 1)
        for l, r in intervals:
            arr[l] += 1
            if r < mx: arr[r + 1] -= 1

        mx = 0
        tot = 0
        for v in arr:
            tot += v
            mx = max(mx, tot)
        return mx

        # minheap solution
        # intervals.sort()
        # minheap = []
        # mx = 0
        # for l, r in intervals:
        #     while minheap and minheap[0] < l: heapq.heappop(minheap)
        #     heapq.heappush(minheap, r)
        #     mx = max(mx, len(minheap))
        # return mx


