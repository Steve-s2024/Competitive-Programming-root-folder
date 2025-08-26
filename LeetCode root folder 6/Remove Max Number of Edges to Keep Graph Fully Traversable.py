# pretty big achievement able to solve a non-trivial union find question using the union find just learned: 6%
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        graph3 = defaultdict(list)
        for t, u, v in edges:
            if t == 1:
                graph1[u-1].append(v-1)
                graph1[v-1].append(u-1)
            if t == 2:
                graph2[u-1].append(v-1)
                graph2[v-1].append(u-1)
            if t == 3:
                graph3[u-1].append(v-1)
                graph3[v-1].append(u-1)

        vis = set()
        res = 0
        def dfs3(node):
            nonlocal res
            for nxt in graph3[node]:
                if (node, nxt) in vis: continue
                vis.add((node, nxt))
                vis.add((nxt, node))
                if uf.find(nxt) == uf.find(node):
                    res += 1
                else:
                    uf.union(node, nxt)
                    dfs3(nxt)
        for i in range(n):
            dfs3(i)

        uf1, uf2 = UnionFind(n), UnionFind(n)
        uf1.parent, uf1.size = uf.parent[:], uf.size[:]
        vis1 = set()
        def dfs1(node):
            nonlocal res
            for nxt in graph1[node]:
                if (node, nxt) in vis1: continue
                vis1.add((node, nxt))
                vis1.add((nxt, node))
                if uf1.find(nxt) == uf1.find(node):
                    res += 1
                else:
                    uf1.union(node, nxt)
                    dfs1(nxt)

        for i in range(n):
            dfs1(i)


        uf2.parent, uf2.size = uf.parent[:], uf.size[:]
        vis2 = set()
        def dfs2(node):
            nonlocal res
            for nxt in graph2[node]:
                if (node, nxt) in vis2: continue
                vis2.add((node, nxt))
                vis2.add((nxt, node))
                if uf2.find(nxt) == uf2.find(node):
                    res += 1
                else:
                    uf2.union(node, nxt)
                    dfs2(nxt)

        for i in range(n):
            dfs2(i)


        a, b = uf1.find(0), uf2.find(0)
        for i in range(n):
            if uf1.find(i) != a or uf2.find(i) != b: return -1
        return res