# dp & do maxHeap and hashMap on dp array to
# maintain maximum value in a fixed length 
# range solution: 10%
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        dp[-1] = nums[-1]
        hashMap = defaultdict(int)
        hashMap[dp[-1]] += 1
        maxHeap = [-nums[n-1]]
        heapq.heapify(maxHeap)
        l, r = n-1, n-1
        while r-l+1 < k and r-l+1 < n:
            l-=1
            dp[l] = nums[l] + -maxHeap[0]
            hashMap[dp[l]] += 1
            heapq.heappush(maxHeap, -dp[l])
        
        # print(maxHeap, hashMap)
        while l > 0:
            l -= 1
            dp[l] = nums[l] + -maxHeap[0]
            hashMap[dp[l]] += 1
            heapq.heappush(maxHeap, -dp[l])
            hashMap[dp[r]] -= 1
            r -= 1
            while maxHeap and hashMap[-maxHeap[0]] == 0:
                heapq.heappop(maxHeap)
        # print(dp)
        return dp[0]
            