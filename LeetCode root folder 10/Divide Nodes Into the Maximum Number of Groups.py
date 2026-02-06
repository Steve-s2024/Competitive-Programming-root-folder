# i definitely excelled myself here. a stroke of genius

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
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        edges = [[u-1, v-1] for u, v in edges]
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mp = defaultdict(set)
        uf = UnionFind(n)
        for u, v in edges: uf.union(u, v)
        for u in range(n): mp[uf.find(u)].add(u)

        def helper(st):
            vs = set()
            fmp = {}
            def dfs(u, f):
                if u in vs: return
                vs.add(u)
                fmp[u] = f
                for v in g[u]: dfs(v, (f+1)%2)
            dfs(list(st)[0], 0)

            for u in st:
                for v in g[u]:
                    # print(u, v, v in st, v in fmp)
                    if fmp[u] == fmp[v]: return -1

            ans = 0
            for src in st:
                vs = {src}
                q = deque([src])
                res = 0
                while q:
                    for _ in range(len(q)):
                        u = q.popleft()
                        for v in g[u]:
                            if v in vs: continue
                            vs.add(v)
                            q.append(v)
                    res += 1
                # print(src, res)
                ans = max(res, ans)
            return ans

        ans = 0
        for e in mp.values():
            res = helper(e)
            if res == -1: return -1
            ans += res
        return ans