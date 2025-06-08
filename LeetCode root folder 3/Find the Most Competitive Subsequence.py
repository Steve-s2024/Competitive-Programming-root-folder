# actual, the question is tailored to mono-stack. very interesting
# I guarantee it is super hard to realize the usage of mono-stack
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        arr = deque()
        n = len(nums)
        l, r = 0, n - k
        res = []
        for i in range(r):
            while arr and arr[-1] > nums[i]:
                arr.pop()
            arr.append(nums[i])

        for i in range(n - k, n):
            while arr and arr[-1] > nums[i]:
                arr.pop()
            arr.append(nums[i])
            res.append(arr[0])
            arr.popleft()

        return res


# dont know why its slow...: 5%
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        minHeap = []
        mp = defaultdict(deque)
        l, r = 0, n - k
        for i in range(r + 1):
            heapq.heappush(minHeap, nums[i])
            mp[nums[i]].append(i)

        for i in range(k):
            while minHeap and len(mp[minHeap[0]]) == 0:
                heapq.heappop(minHeap)

            mi = minHeap[0]
            idx = mp[mi][0]
            res.append(mi)
            for j in range(l, idx + 1):
                mp[nums[j]].popleft()
            if r >= n - 1:
                break
            heapq.heappush(minHeap, nums[r + 1])
            mp[nums[r + 1]].append(r + 1)
            l, r = idx + 1, r + 1

        return res


# brute force greedy TLE:
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        l, r = 0, n-k
        for i in range(n):
            idx, mi = l, nums[l]
            for j in range(l, r+1):
                if nums[j] < mi:
                    mi = nums[j]
                    idx = j
            res.append(mi)
            l, r = idx, r+1
        return res