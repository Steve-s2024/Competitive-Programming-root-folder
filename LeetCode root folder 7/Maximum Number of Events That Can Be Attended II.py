# 49%
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        mp = {}
        minheap = []
        for i in range(n):
            l, r, _ = events[i]
            while minheap and minheap[0][0] < l:
                _, j = heapq.heappop(minheap)
                mp[j] = i
            heapq.heappush(minheap, (r, i))
        while minheap:
            _, j = heapq.heappop(minheap)
            mp[j] = n
        @cache
        def recursive(i, k):
            nonlocal n
            if i >= n: return 0
            res = recursive(i+1, k)
            if k > 0: res = max(res, recursive(mp[i], k-1) + events[i][2])
            return res
        return recursive(0, k)
