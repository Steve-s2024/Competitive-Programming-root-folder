# binary search and maxHeap: 39%
# a very interesting fact, at first try I forget to make m = (l+r)//2
# instead I made it look like m = (l+r), but mysteriously it did work
# only that it hit TLE on the very last few testcases...
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.arr = []
        n = len(persons)
        maxHeap = []
        mp = defaultdict(int)
        for i in range(n):
            mp[persons[i]] += 1
            while maxHeap and -maxHeap[0][0] <= mp[persons[i]]:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-mp[persons[i]], persons[i]))

            self.arr.append((times[i], maxHeap[0][1]))

    def q(self, t: int) -> int:
        arr = self.arr
        l, r = 0, len(arr) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= t:
                res = m
                l = m + 1
            else:
                r = m - 1

        return arr[res][1]
