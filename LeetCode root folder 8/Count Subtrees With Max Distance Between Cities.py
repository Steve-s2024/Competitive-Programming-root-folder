# this is absolutely annoying to implement, union find, bfs find tree diameter solution: 12%
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def bfs(self, g, n):
        deg = [len(r) for r in g]
        vis = [0] * n
        q = deque()
        for u in range(n):
            if deg[u] == 1:
                vis[u] = 1
                q.append(u)

        res = 0
        while q:
            l = len(q)
            for _ in range(l):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]: continue
                    deg[v] -= 1
                    if deg[v] == 1:
                        vis[v] = 1
                        q.append(v)
            if l == 1 and not q: return 2 * res
            if l == 2 and not q: return 2 * res + 1
            res += 1
        return 0

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * (n - 1)
        for mask in range(1, 1 << n):
            g = [[] for _ in range(n)]
            uf = UnionFind(n)
            for u, v in edges:
                u, v = u - 1, v - 1
                if (1 << u) & mask and (1 << v) & mask:
                    g[u].append(v)
                    g[v].append(u)
                    uf.union(u, v)

            lowbit = mask & (~(mask - 1))
            p = uf.find(lowbit.bit_length() - 1)
            if uf.size[p] != mask.bit_count(): continue

            mx = self.bfs(g, n)
            if mx == 0: continue
            ans[mx - 1] += 1
        return ans