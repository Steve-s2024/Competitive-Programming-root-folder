# optimized greedy solution, pretty tough question: 6%
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1: return target[0] == 1

        maxHeap = []
        for num in target: heapq.heappush(maxHeap, -num)

        sm = sum(target)
        while len(maxHeap) >= 2:
            a, b = -heapq.heappop(maxHeap), -maxHeap[0]
            incre = sm - a
            dif = a - b
            mul = dif // incre + 1

            decre = mul * incre
            a -= decre
            heapq.heappush(maxHeap, -a)
            if a < 1: break
            sm -= decre

        cnt = 0
        sm = 0
        while maxHeap:
            a = -heapq.heappop(maxHeap)
            if a != 1:
                cnt += 1
            sm += a
        return sm == 1 and cnt <= 1



# greedy approach, reverse engineering: TLE on [1, 100000000]
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap = []
        for num in target: heapq.heappush(maxHeap, -num)

        sm = sum(target)
        while maxHeap:
            a = -heapq.heappop(maxHeap)
            if a == 1: return True
            b = a - (sm - a)
            if b < 1: return False
            sm -= a
            sm += b
            heapq.heappush(maxHeap, -b)

        return True

