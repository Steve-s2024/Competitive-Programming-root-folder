# pretty clear priority queue question, but took me a while to realize...
# and before that I was trying greedy:877
# ms
# Beats
# 5.92%
class Solution:
    def findScore(self, nums: List[int]) -> int:
        minHeap = []
        marked = set()
        heapq.heapify(minHeap)
        for i in range(len(nums)):
            heapq.heappush(minHeap, [nums[i], i])
        res = 0
        while minHeap:
            cur = heapq.heappop(minHeap)
            i = cur[1]
            if i not in marked:
                res += cur[0]
                marked.add(i-1)
                marked.add(i)
                marked.add(i+1)
        return res