# the question is deceptively easy, simple minHeap solution, once you translate
# it into a question to sorting and judging if event can be attended: 37%
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        day = max(e[1] for e in events)
        res = 0
        j = 0
        events.sort(key=lambda i: (i[0], i[1]))
        minHeap = []

        for i in range(1, day + 1):
            while j < len(events) and events[j][0] <= i:
                heapq.heappush(minHeap, events[j][1])
                j += 1
            while minHeap and minHeap[0] < i:
                heapq.heappop(minHeap)
            if minHeap:
                heapq.heappop(minHeap)
                res += 1

        return res

