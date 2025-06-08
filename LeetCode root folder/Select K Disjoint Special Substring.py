# incomplete
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        hashMap = defaultdict(list)
        for i, c in enumerate(s):
            hashMap[c].append(i)

        heap = []
        heapq.heapify(heap)
        max_ = 0
        for val in hashMap.values():
            i1, i2 = val[0], val[-1]
            while heap and heap[0] < i1:
                heapq.heappop(heap)
            heapq.heappush(heap, i2)
            max_ = max(len(heap), max_)
        print(len(hashMap), max_, k)
        return len(hashMap) - (max_-1) >= k

