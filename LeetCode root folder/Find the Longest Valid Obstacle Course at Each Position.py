


# monotonic stack & priority queue and dp, but not 
# the way.
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        record = [-1] * n
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in range(n-1, -1, -1):
            while maxHeap and maxHeap[0][1] >= obstacles[i]:
                cur = heapq.heappop(maxHeap)
                record[cur[0]] = i
            heapq.heappush(maxHeap, (i, obstacles[i]))
        # print(record)

        dp = [0] * n
        for i in range(n):
            left = record[i]
            if left == -1:
                dp[i] = 1
            else:
                dp[i] = dp[left] + 1
        # print(dp)
        return dp