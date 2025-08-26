# very intricate joining of dp and priority queue, interesting for that reason: 30%
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = nums[:]
        maxheap = []
        for i in range(n):
            while maxheap and i - maxheap[0][1] > k: heapq.heappop(maxheap)
            if maxheap:
                mx = -maxheap[0][0]
                if mx > 0: dp[i] += mx
            heapq.heappush(maxheap, (-dp[i], i))
        return max(dp)

