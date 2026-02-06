# absolutely not my issue the code is 80 lines long. this problem took half my brain cell
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
    def dfs(self, u, tree):
        res = 0
        for v in tree[u]:
            res = max(self.dfs(v, tree), res)
        return res + 1

    def check(self, ndes, g):
        n = len(ndes)
        ds = defaultdict(int)
        for u in ndes: ds[g[u][0]] += 1
        vs = set()
        q = deque()
        for u in ndes:
            d = ds[u]
            if d == 0:
                q.append(u)
                vs.add(u)
        while q:
            u = q.popleft()
            for v in g[u]:
                ds[v] -= 1
                if ds[v] == 0:
                    vs.add(v)
                    q.append(v)
        x = len(vs)
        if n - x == 2:
            ar = []
            tree = defaultdict(list)
            for u in ndes:
                if u not in vs: ar.append(u)
            for u in ndes:
                for v in g[u]:
                    if v in ar and u in ar: continue
                    tree[v].append(u)
            a, b = self.dfs(ar[0], tree)-1, self.dfs(ar[1], tree)-1
            # print(ar, a, b)
            return 2 + a + b, 1
        return n - x, 0

    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        uf = UnionFind(n)
        g = [[] for _ in range(n)]
        for i, f in enumerate(fav):
            g[i].append(f)
            uf.union(i, f)

        mp = defaultdict(list)
        for u in range(n): mp[uf.find(u)].append(u)
        res = 0
        two = 0
        for val in mp.values():
            x, f = self.check(val, g)
            if f: # cycle of two
                two += x
            else: res = max(res, x)
        return max(res, two)












# incorrect solution
# I was thinking it as a 1D cycle detection problem, but maybe it is actually a 2D graph BFS problem
class Solution:
    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        vs = [0] * n
        res = 0
        for u in range(n):
            cr = u
            st = u
            prv = -1
            x = 0
            ar = []
            while vs[cr] == 0:
                ar.append(cr)
                vs[cr] = 1
                prv = cr
                cr = fav[cr]
                x += 1
            # print(cr, [st, prv])
            if fav[cr] == prv or cr == st: # valid seating
                res = max(res, x)

        return res