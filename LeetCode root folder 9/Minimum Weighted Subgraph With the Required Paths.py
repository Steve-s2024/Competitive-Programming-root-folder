# neat problem, thinking in reverse way combined in the forward direction will help a lot.
# one think need notice is that such minimum weighted subgraph is always a tree (proven by contradiction)
class Solution:
    def dijkstra(self, g, src):
        n = len(g)
        hp = [(0, src)]
        mp = {}
        vs = [0] * n
        while hp:
            wei, u = heappop(hp)
            if vs[u]: continue
            vs[u] = 1
            mp[u] = wei
            for v, w in g[u]: heappush(hp, (wei + w, v))
        # print(mp)
        return mp

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            rev[v].append((u, w))

        mp1, mp2, mp3 = self.dijkstra(g, src1), self.dijkstra(g, src2), self.dijkstra(rev, dest)

        res = inf
        for i in range(n):
            if i in mp1 and i in mp2 and i in mp3:
                res = min(mp1[i] + mp2[i] + mp3[i], res)
        return res if res != inf else -1



