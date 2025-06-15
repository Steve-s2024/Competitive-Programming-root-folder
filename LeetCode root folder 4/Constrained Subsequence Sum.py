# dp, maxHeap + deque + frequency map maintaining window maximum element: 27%
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
            heapq.heappush(maxHeap, -dp[i])
            q.append(dp[i])
            mp[dp[i]] += 1

            if len(q) > k:
                mp[q.popleft()] -= 1
        # print(dp)
        return max(dp)