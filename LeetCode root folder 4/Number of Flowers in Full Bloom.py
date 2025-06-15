# 8%, took advantage of my advance interval merging template
class Solution:
    @staticmethod
    def merge(arr):
        arr = arr[:]
        arr.sort(key=lambda i: i[0])
        inf = float('inf')
        arr.append((inf, inf))
        minHeap = []
        intervals = []
        weights = []
        L, R = arr[0]
        for l, r in arr:
            while minHeap and minHeap[0] < l:
                R = heapq.heappop(minHeap)
                if L <= R:
                    weights.append(len(minHeap) + 1)
                    intervals.append((L, R))
                L = R + 1
            if l > L:
                weights.append(len(minHeap))
                intervals.append((L, l - 1))
            L = l
            heapq.heappush(minHeap, r)

        intervals.pop()
        weights.pop()
        # print(intervals, weights)
        return intervals, weights

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        intervals, weights = Solution.merge(flowers)
        n = len(intervals)
        ans = [0] * len(people)
        for i, p in enumerate(people):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if p in range(intervals[m][0], intervals[m][1] + 1):
                    ans[i] = weights[m]
                    break
                elif p < intervals[m][0]:
                    r = m - 1
                else:
                    l = m + 1

        return ans
