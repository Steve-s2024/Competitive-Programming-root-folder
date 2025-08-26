# weird that the Djikstra hit TLE without the visited set
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        minheap = [(1, 0, 0, 1)]
        vis = set()
        vis.add((0, 0))
        while minheap:
            cost, r, c, t = heapq.heappop(minheap)
            if r == m - 1 and c == n - 1: return cost

            if t % 2 == 1:
                for R, C in [(r + 1, c), (r, c + 1)]:
                    if R in range(m) and C in range(n) and (R, C) not in vis:
                        vis.add((R, C))
                        heapq.heappush(minheap, (cost + (R + 1) * (C + 1), R, C, t + 1))
            else:
                heapq.heappush(minheap, (cost + waitCost[r][c], r, c, t + 1))

