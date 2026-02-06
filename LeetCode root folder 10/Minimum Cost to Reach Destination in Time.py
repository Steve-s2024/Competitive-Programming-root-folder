# dp, i think the only reason this solution is not O(n^3) is because the constraint edges.length <= 1000
# which means in worst case (when graph is complete), number of vertices is <= sqrt(1000) ~32
# if they every push the limit edges.length <= 1e5 level, this will not work
class Solution:
    def minCost(self, mxt: int, edges: List[List[int]], pf: List[int]) -> int:
        n = len(pf)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])

        @cache
        def dfs(u, t):
            nonlocal n, mxt
            if u == n - 1: return 0
            res = inf
            for v, w in g[u]:
                if t + w > mxt: continue
                res = min(res, dfs(v, t + w) + pf[v])
            return res

        res = dfs(0, 0) + pf[0]
        return res if res != inf else -1


# no idea why this comparator works (in Dijkstra), but it worked. credit comment post
# no idea for this, but after some thinking I came up with an easier but less efficient dp solution
class Solution:
    def minCost(self, mxt: int, edges: List[List[int]], pf: List[int]) -> int:
        n = len(pf)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])


        vs = [inf]*n
        hp = [(pf[0], 0, 0)]
        while hp:
            c, t, u = heappop(hp)
            t = -t
            if u == n - 1: return c
            if vs[u] <= t: continue
            vs[u] = t
            for v, w in g[u]:
                if t + w <= mxt:
                    heappush(hp, (c + pf[v], -(t + w), v))
        return -1
