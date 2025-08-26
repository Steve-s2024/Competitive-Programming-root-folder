# pretty intuitive, maybe that's why it got a lot upvote.: 18%
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        x = n // 3
        forward = [inf] * n
        sm = 0
        maxheap = []
        for i in range(n):
            heapq.heappush(maxheap, -nums[i])
            sm += nums[i]
            if len(maxheap) > x: sm -= -heapq.heappop(maxheap)
            if len(maxheap) == x: forward[i] = sm

        backward = [-inf] * n
        sm = 0
        minheap = []
        for i in range(n - 1, -1, -1):
            heapq.heappush(minheap, nums[i])
            sm += nums[i]
            if len(minheap) > x: sm -= heapq.heappop(minheap)
            if len(minheap) == x: backward[i] = sm

        # print(forward)
        # print(backward)
        ans = inf
        for i in range(x, n - x + 1):
            ans = min(ans, forward[i - 1] - backward[i])
        return ans