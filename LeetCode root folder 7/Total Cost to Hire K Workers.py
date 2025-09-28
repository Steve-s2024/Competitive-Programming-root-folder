# boring low rating question.: 18%
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        q = deque(costs)
        minheap = []
        for i in range(candidates):
            if not q: break
            heapq.heappush(minheap, (q.popleft(), i, 1))
            if not q: break
            heapq.heappush(minheap, (q.pop(), n-1-i, 2))

        res = 0
        i1, i2 = candidates, n-1-candidates
        for i in range(k):
            num, _, side = heapq.heappop(minheap)
            res += num
            if side == 1 and q:
                heapq.heappush(minheap, (q.popleft(), i1, 1))
                i1 += 1
            if side == 2 and q:
                heapq.heappush(minheap, (q.pop(), i2, 2))
                i2 -= 1
        return res