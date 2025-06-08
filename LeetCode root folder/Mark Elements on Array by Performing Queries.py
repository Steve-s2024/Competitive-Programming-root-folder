# boring priority queue question | solution:1949
# ms
# Beats
# 37.93%
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        for idx, num in enumerate(nums):
            hashMap[num].append(idx)
        minHeap = [(key, sorted(val, reverse=True)) for key, val in hashMap.items()]
        heapq.heapify(minHeap)
        # print(minHeap)
        marked = set()
        sum_ = sum(nums)
        ans = []
        for i, k in queries:
            if i not in marked:
                marked.add(i)
                sum_ -= nums[i]
            while k and minHeap:
                while minHeap[0][1] and k:
                    cur = minHeap[0][1].pop()
                    if cur not in marked:
                        marked.add(cur)
                        sum_ -= minHeap[0][0]
                        k -= 1
                if len(minHeap[0][1]) == 0:
                    heapq.heappop(minHeap)
            ans.append(sum_)
        return ans