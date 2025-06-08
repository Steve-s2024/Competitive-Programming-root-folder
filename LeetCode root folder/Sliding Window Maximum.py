# hash table & max heap & sliding window solution:383
# ms
# Beats
# 15.82%
from collections import defaultdict
import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        hashMap = defaultdict(int)
        res = []
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            hashMap[nums[i]] += 1
        # print(hashMap, maxHeap)

        res.append(-maxHeap[0])
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, -nums[i])
            hashMap[nums[i - k]] -= 1
            hashMap[nums[i]] += 1
            while hashMap[-maxHeap[0]] == 0:
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0])

        return res



# from NeetCode, sliding window & monotonic queue solution:215
# ms
# Beats
# 27.31%
'''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque([])
        res = []
        idx = 0
        for num in nums[:k]:
            while window and window[-1][1] < num:
                window.pop()
            window.append([idx, num])
            idx += 1

        res.append(window[0])
        for num in nums[k:]:
            if window and window[0][0] <= idx-k:
                window.popleft()
            while window and window[-1][1] < num:
                window.pop()
            window.append([idx, num])
            res.append(window[0])
            idx += 1
        return [ele for idx, ele in res]'''