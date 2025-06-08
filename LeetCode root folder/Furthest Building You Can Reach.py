# turns out only greedy and minHeap is enough: 9%
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        res = 0
        minHeap = []
        heapq.heapify(minHeap)
        totalDiff = 0
        ladderCancel = 0
        for i in range(1, n):
            diff = max(0, heights[i]-heights[i-1])
            totalDiff += diff
            ladderCancel += diff
            heapq.heappush(minHeap, diff)
            if len(minHeap) > ladders:
                ladderCancel -= heapq.heappop(minHeap)
            if totalDiff - ladderCancel <= bricks:
                res = i
            else:
                break
        return res
 

# standard binary search and simulate(greedy) solution: 5%
# clearly there is a better way
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l, r = 0, n-1
        res = 0
        while l <= r:
            m = (l+r)//2
            # pretend m as the farthest building can be reached
            diff = []
            for i in range(1, m+1):
                if heights[i] > heights[i-1]:
                    diff.append(heights[i]-heights[i-1])
            diff.sort(reverse = True)
            bricksCost = sum(diff[ladders:])
            if bricksCost > bricks:
                r = m-1
            else:
                res = m
                l = m+1
        return res