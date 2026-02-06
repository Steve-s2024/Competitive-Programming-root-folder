# I crushed this problem under 20 minutes, though taking a bit hint from neetcode to use DSU
# nonetheless, this is a 2450 rated gruesome problem! so far the highest rated problem solved

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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = UnionFind(n)
        mp = defaultdict(list)
        for u in range(n): mp[vals[u]].append(u)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        res = 0
        ar = list(mp.keys())
        ar.sort()
        for ct in ar:
            for u in mp[ct]:
                for v in g[u]:
                    if vals[v] <= vals[u]: uf.union(u, v)

            tmp = defaultdict(int)
            for u in mp[ct]: tmp[uf.find(u)] += 1
            for val in tmp.values(): res += val * (val - 1) // 2

        return res + n