# minHeap solution, count the maximum number of overlapping of intervals:435
# ms
# Beats
# 20.10%
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        intervals = []
        for num in nums:
            intervals.append((num-k, num+k))
        intervals.sort(key = lambda i : i[0])
        res = 0
        minHeap = []
        heapq.heapify(minHeap)
        for l, r in intervals:
            heapq.heappush(minHeap, r)
            while minHeap[0] < l:
                heapq.heappop(minHeap)
            res = max(res, len(minHeap))
        return res
