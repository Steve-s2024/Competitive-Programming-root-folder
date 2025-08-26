# didn't use the merging template like in the old code, and therefore faster: 55%
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(people)
        people = [(people[i], i) for i in range(n)]
        people.sort(key = lambda i:i[0])
        flowers.sort(key = lambda i:i[0])
        res = [0]*n
        minheap = []
        i = 0
        size = len(flowers)
        for p, idx in people:
            while i < size and flowers[i][0] <= p:
                heapq.heappush(minheap, flowers[i][1])
                i += 1
            while minheap and minheap[0] < p: heapq.heappop(minheap)
            res[idx] = len(minheap)
        return res