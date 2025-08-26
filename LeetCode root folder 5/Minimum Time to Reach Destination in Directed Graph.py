# the first time I wasted time on worrying the code may it TLE and trying to optimize it, but it didn't hit TLE...
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)
        graph = defaultdict(set)
        for u, v, a, b in edges:
            graph[u].add(v)
            mp[(u, v)].append((a, b))

        minheap = [(0, 0)]
        vis = set()
        while minheap:
            t, u = heapq.heappop(minheap)
            if u == n - 1: return t
            for v in graph[u]:
                if (u, v) in vis: continue
                vis.add((u, v))
                for a, b in mp[(u, v)]:
                    if t > b: continue
                    heapq.heappush(minheap, (max(t, a) + 1, v))

        return -1