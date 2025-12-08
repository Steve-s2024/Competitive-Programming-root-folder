# not too hard dijkstra idea.

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        minheap = [(0, 0)]
        vis = [0] * n
        mp = defaultdict(int)
        while minheap:
            l, u = heappop(minheap)
            if vis[u]: continue
            vis[u] = 1
            for v, w in g[u]:
                mp[(u, v)] += maxMoves - l
                mp[(v, u)] += maxMoves - l
                if vis[v]: continue
                if l + w + 1 <= maxMoves: heappush(minheap, (l + w + 1, v))

        # print(vis)
        # print(mp)
        res = sum(vis)
        for u, v, w in edges: res += min(w, mp[(u, v)])
        return res
