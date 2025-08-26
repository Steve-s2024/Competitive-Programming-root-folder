# MLE on simple Dijkstra, fortunately I know exactly why it hit MLE, so didn't take too long to fix the code
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w, 1))
            graph[v].append((u, w, 2))

        minheap = [(0, 0)]
        vis = {}
        vis[0] = 0
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node == n-1: return cost
            for nxt, wei, typ in graph[node]:
                if typ == 1: newC = cost+wei
                else: newC = cost+2*wei
                if nxt in vis and vis[nxt] <= newC: continue
                vis[nxt] = newC
                heapq.heappush(minheap, (newC, nxt))

        return -1