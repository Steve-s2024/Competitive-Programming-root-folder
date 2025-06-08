# sliding window & min, max heap, took me a while to 
# coordinate all the details though:
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        res = 0
        minHeap, maxHeap = [], []
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        hashMap = defaultdict(int)
        while r < n:
            hashMap[nums[r]] += 1
            heapq.heappush(minHeap, nums[r])
            heapq.heappush(maxHeap, -nums[r])
            while l < r and max(
                abs(minHeap[0]-nums[r]) if minHeap else 0, 
                abs(-maxHeap[0]-nums[r]) if maxHeap else 0
            ) > 2:
                hashMap[nums[l]] -= 1
                while minHeap and hashMap[minHeap[0]] == 0:
                    heapq.heappop(minHeap)
                while maxHeap and hashMap[-maxHeap[0]] == 0:
                    heapq.heappop(maxHeap)
                l += 1

            # print(l, r)
            size = r-l+1
            res += size
            r += 1
            
        return res  