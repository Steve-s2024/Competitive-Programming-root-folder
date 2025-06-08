# dynamic minHeap solution, basically just minHeap maintaining the 
# state of apples and modify the apple count in the heap at
# the sametime: 71%
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        day = 0
        n = len(apples)
        res = 0
        while day < n:
            heapq.heappush(minHeap, [day+days[day], apples[day]])
            while minHeap and minHeap[0][0] <= day:
                heapq.heappop(minHeap)
            if minHeap:
                minHeap[0][1]-=1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
                res+=1
            day+=1
        
        while minHeap:
            while minHeap and minHeap[0][0] <= day:
                heapq.heappop(minHeap)
            if minHeap:
                minHeap[0][1]-=1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
                res+=1
            day+=1

        return res 