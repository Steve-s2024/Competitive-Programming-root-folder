'''wow'''
'''
  __________________
 | ________________ |
 ||          ____  ||
 ||   /\    |      ||
 ||  /__\   |      ||
 || /    \  |____  ||
 ||________________||
 |__________________|
 \###################\
  \###################\
   \        ____       \
    \_______\___\_______\
An AC a day keeps the doctor away. (tin_le)
'''

from collections import defaultdict, deque, Counter
from typing import List
from sortedcontainers import SortedList
import heapq, cmath, sys
sys.setrecursionlimit(1 << 15)


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        q = deque()
        maxHeap = []
        mp = defaultdict(int)
        for i in range(n-1, -1, -1):
            while maxHeap and mp[-maxHeap[0]] == 0: heapq.heappop(maxHeap)
            if maxHeap and -maxHeap[0] > 0:
                dp[i] += -maxHeap[0]
            dp[i] += nums[i]
            heapq.heappush(maxHeap, -nums[i])
            q.append(nums[i])
            mp[nums[i]] += 1

            if len(q) >= k:
                mp[q.popleft()] -= 1
        print(dp)