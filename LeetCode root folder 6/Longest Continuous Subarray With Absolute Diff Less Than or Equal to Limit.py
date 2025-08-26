# with sorted set -SortedList, it is much cleaner and easier: 5%
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        j = -1
        sl = SortedList()
        res = 0
        for i in range(n):
            while not sl or sl[-1] - sl[0] <= limit:
                j += 1
                if j >= n: break
                sl.add(nums[j])
            # print(i)
            # print(sl)
            res = max(res, j-i)
            sl.remove(nums[i])
        return res

# what a long name, and the implementation is very boring: 43%
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        j = -1
        minheap = []
        maxheap = []
        mp = defaultdict(int)
        res = 0
        for i in range(n):
            while minheap and mp[minheap[0]] == 0: heapq.heappop(minheap)
            while maxheap and mp[-maxheap[0]] == 0: heapq.heappop(maxheap)

            while 1:
                j += 1
                if j >= n: break
                mp[nums[j]] += 1
                heapq.heappush(minheap, nums[j])
                heapq.heappush(maxheap, -nums[j])
                if -maxheap[0] - minheap[0] > limit: break
            res = max(res, j - i)
            mp[nums[i]] -= 1

        return res