
# TLE on 16th...

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        minheap = [(0, 1)]
        res = inf
        while minheap:
            t, node = heapq.heappop(minheap)
            if node == n:
                if res < t:
                    return t
                else:
                    res = t
            mul = (t // change)
            if mul % 2 == 1:
                for nxt in graph[node]:
                    heapq.heappush(minheap, ((mul + 1) * change + time, nxt))
            else:
                for nxt in graph[node]:
                    heapq.heappush(minheap, (t + time, nxt))
