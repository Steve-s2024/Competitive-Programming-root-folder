# why the fk am I sooooooo fking smarttttotootototototototo!!!!!!!!!: 92%
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)

        arr = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        arr.sort(key=lambda i: i[0])
        maxheap = []
        totQ = 0
        res = inf
        for i in range(n):
            r, q = arr[i]
            heapq.heappush(maxheap, -q)
            totQ += q
            if len(maxheap) > k:
                totQ -= -heapq.heappop(maxheap)
            if len(maxheap) == k:
                res = min(res, r * totQ)

        return res





# brute force TLE
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)

        res = inf
        for i in range(n):
            rate = wage[i] / quality[i]
            cands = []
            for j in range(n):
                curRate = wage[j] / quality[j]
                if curRate > rate: continue
                cands.append(quality[j])

            if len(cands) < k: continue
            # print(i, cands)
            cands.sort()
            totalQ = sum(cands[:k])
            totalC = totalQ * rate
            res = min(res, totalC)

        return res

