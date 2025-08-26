# the proper way to do it, the state of DP can be even reduced. the time in the state is not necessary since we are
# doing BFS instead of Dijkstra: 55%
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(i, 1<<i) for i in range(n)])
        vis = set()
        res = 0
        while q:
            for _ in range(len(q)):
                node, mask = q.popleft()
                if mask == (1<<n)-1: return res
                for nxt in graph[node]:
                    state = (nxt, mask | (1<<nxt))
                    if state in vis: continue
                    vis.add(state)
                    q.append((nxt, mask | (1<<nxt)))
            res += 1



# could just use deque: 9%
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(0, i, 1<<i) for i in range(n)])
        vis = set()
        while q:
            t, node, mask = q.popleft()
            if mask == (1<<n)-1: return t
            for nxt in graph[node]:
                state = (t+1, nxt, mask | (1<<nxt))
                if state in vis: continue
                vis.add(state)
                q.append((t+1, nxt, mask | (1<<nxt)))



# optimization with DP visited set, somehow worked??: 7%
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        minheap = [(0, i, 1<<i) for i in range(n)]
        heapq.heapify(minheap)
        vis = set()
        while minheap:
            t, node, mask = heapq.heappop(minheap)
            if mask == (1<<n)-1: return t
            for nxt in graph[node]:
                state = (t+1, nxt, mask | (1<<nxt))
                if state in vis: continue
                vis.add(state)
                heapq.heappush(minheap, (t+1, nxt, mask | (1<<nxt)))






# Dijkstra & bit-mask, TLE
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        minheap = [(0, i, 1<<i) for i in range(n)]
        heapq.heapify(minheap)

        while minheap:
            t, node, mask = heapq.heappop(minheap)
            if mask == (1<<n)-1: return t
            for nxt in graph[node]:
                heapq.heappush(minheap, (t+1, nxt, mask | (1<<nxt)))

