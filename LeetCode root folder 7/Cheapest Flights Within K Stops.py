# Bellman Ford, handles negative weights. time is O(k*E), the runtime may not be faster: 32%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [inf]*n
        tmp = [inf]*n
        arr[src] = 0
        for i in range(k+1):
            for u, v, p in flights:
                tmp[v] = min(tmp[v], arr[u]+p)
            arr = tmp[:]
        return arr[dst] if arr[dst] != inf else -1


# Dijkstra with DP state pruning, using Bellman Ford should give much faster runtime: 47%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))

        minheap = [(0, 0, src)]
        vis = {}
        while minheap:
            cost, cnt, node = heapq.heappop(minheap)
            if node == dst: return cost
            if cnt > k: continue
            for nxt, price in graph[node]:
                state = (cnt+1, nxt)
                if state in vis and vis[state] <= cost+price: continue
                vis[state] = cost+price
                heapq.heappush(minheap, (cost+price, cnt+1, nxt))
        return -1